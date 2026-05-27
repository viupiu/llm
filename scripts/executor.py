import subprocess
import shlex

def run_opencode(prompt: str, agent: str = "build") -> str:
    try:
        proc = subprocess.run(
            [
                OPENCODE,
                "run",
                "--agent",
                agent,
                prompt,
            ],
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