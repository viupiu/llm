import subprocess
import traceback
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from scripts.config import TOKEN


# -----------------------------
# SETTINGS
# -----------------------------

# Если "opencode.cmd" не найдется из Python,
# замени на полный путь, например:
# OPENCODE = r"C:\Users\Mariyaa\AppData\Roaming\npm\opencode.cmd"
OPENCODE = "opencode.cmd"

# Папка проекта, из которой нужно запускать opencode и git.
# Сейчас используется текущая папка запуска скрипта.
# Можно явно указать:
# PROJECT_DIR = r"C:\Users\Mariyaa\Desktop\скрипты\LLM"
PROJECT_DIR = os.getcwd()


# -----------------------------
# OPENCODE EXECUTOR
# -----------------------------

def run_opencode(prompt: str, agent: str = "build") -> str:
    try:
        cmd = [
            OPENCODE,
            "run",
            "--agent",
            agent,
            prompt,
        ]

        print("[OPENCODE CMD]", cmd)

        proc = subprocess.run(
            cmd,
            cwd=PROJECT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=180,
            shell=False,
        )

        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()

        print("[OPENCODE RETURN]", proc.returncode)
        print("[OPENCODE STDOUT]", out[:1000])
        print("[OPENCODE STDERR]", err[:1000])

        if proc.returncode != 0:
            return (
                "❌ opencode error:\n"
                f"returncode: {proc.returncode}\n\n"
                f"{err or out or 'no output'}"
            )

        return out or err or "⚠️ empty response from opencode"

    except subprocess.TimeoutExpired:
        return "❌ opencode timeout"

    except FileNotFoundError as e:
        return (
            "❌ executor crash:\n"
            "Python не нашел opencode.cmd.\n\n"
            f"details: {str(e)}"
        )

    except Exception as e:
        return f"❌ executor crash:\n{str(e)}"

# -----------------------------
# SAFE SHELL
# -----------------------------

def run_shell(cmd: list) -> str:
    try:
        result = subprocess.run(
            cmd,
            cwd=PROJECT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            shell=False,
        )

        out = (result.stdout or "").strip()
        err = (result.stderr or "").strip()

        if result.returncode != 0:
            return f"❌ ERROR:\n{err or out or 'no output'}"

        return out or "✓ done"

    except Exception as e:
        return f"❌ EXCEPTION:\n{str(e)}"


def run_cmd(command: str) -> str:
    """
    Для Windows-команд типа where.
    """
    try:
        result = subprocess.run(
            ["cmd", "/c", command],
            cwd=PROJECT_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            shell=False,
        )

        out = (result.stdout or "").strip()
        err = (result.stderr or "").strip()

        if result.returncode != 0:
            return f"❌ CMD ERROR:\n{err or out or 'no output'}"

        return out or "✓ done"

    except Exception as e:
        return f"❌ CMD EXCEPTION:\n{str(e)}"


# -----------------------------
# SIMPLE ROUTER
# -----------------------------

def process(text: str) -> str:
    text = text.strip()
    low = text.lower()

    # HELP
    if low in ["/help", "help"]:
        return (
            "🤖 ORCHESTRATOR\n\n"
            "Команды:\n"
            "/help - помощь\n"
            "/status - git status\n"
            "/where - показать где находится opencode\n"
            "/version - версия opencode\n"
            "/pwd - текущая рабочая папка бота\n"
            "/analyze <text> - простой анализ текста\n\n"
            "Любой другой текст будет отправлен в opencode."
        )

    # DIAGNOSTICS
    if low == "/pwd":
        return f"📁 PROJECT_DIR:\n{PROJECT_DIR}"

    if low == "/where":
        return run_cmd("where opencode && where opencode.cmd")

    if low == "/version":
        return run_shell([OPENCODE, "--version"])

    # GIT
    if low == "/status":
        return run_shell(["git", "status", "--short"])

    # ANALYZE
    if low.startswith("/analyze"):
        content = text.replace("/analyze", "", 1).strip()

        if not content:
            return "⚠️ no text provided"

        return (
            "🧠 ANALYSIS\n\n"
            f"words: {len(content.split())}\n"
            f"chars: {len(content)}\n"
            f"preview: {content[:80]}"
        )

    # SIMPLE INTENT ROUTING
    if "ошибка" in low:
        return run_opencode(
            "Analyze this error and propose fix:\n" + text,
            agent="build",
        )

    if "бот" in low:
        return run_opencode(text, agent="build")

    if "создай" in low:
        return run_opencode(
            "Create based on request:\n" + text,
            agent="build",
        )

    # DEFAULT → OPENCODE
    return run_opencode(text, agent="build")


# -----------------------------
# TELEGRAM HANDLERS
# -----------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Orchestrator online\n\n"
        "Напиши /help для списка команд."
    )


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text

    print(f"[IN] {text}")

    try:
        result = process(text)
    except Exception:
        print(traceback.format_exc())
        result = "❌ runtime error"

    if not result or not str(result).strip():
        result = "⚠️ empty response"

    result = str(result)

    # Telegram limit ~4096 chars
    if len(result) <= 4000:
        await update.message.reply_text(result)
    else:
        chunks = [result[i:i + 4000] for i in range(0, len(result), 4000)]

        for chunk in chunks[:3]:
            await update.message.reply_text(chunk)

        if len(chunks) > 3:
            await update.message.reply_text(
                f"⚠️ Output too long. Shown first 3 chunks of {len(chunks)}."
            )


# -----------------------------
# MAIN
# -----------------------------

def main():
    print("=== ORCHESTRATOR START ===")
    print(f"PROJECT_DIR: {PROJECT_DIR}")
    print(f"OPENCODE: {OPENCODE}")

    if not TOKEN:
        raise Exception("TELEGRAM_TOKEN is not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Важно: filters.TEXT без ~filters.COMMAND,
    # чтобы /help, /status, /where тоже попадали в handle.
    app.add_handler(MessageHandler(filters.TEXT, handle))

    print("=== RUNNING ===")
    app.run_polling()


if __name__ == "__main__":
    main()