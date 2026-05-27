import subprocess
from pathlib import Path

# -------------------------
# REGISTRY (твоя карта агентов)
# -------------------------

REGISTRY = {
    "architect": "agents/2_ARCHITECT.md",
    "creative": "agents/3_CREATIVE.md",
    "rules_author": "agents/4_RULES_AUTHOR.md",
    "examples_author": "agents/5_EXAMPLES_AUTHOR.md",
    "copywriter": "agents/6_COPYWRITER.md",
    "responses_author": "agents/7_RESPONSES_AUTHOR.md",
    "validator": "agents/8_VALIDATOR.md",
}


# -------------------------
# LOAD PROMPT
# -------------------------

def load_prompt(agent_name: str, user_text: str) -> str:
    path = Path(REGISTRY.get(agent_name))

    if not path.exists():
        raise Exception(f"Agent file not found: {path}")

    system_prompt = path.read_text(encoding="utf-8")

    return f"""
{system_prompt}

-------------------------
USER REQUEST:
{user_text}
"""


# -------------------------
# RUN OPENCODE
# -------------------------

def run_opencode(prompt: str) -> str:
    result = subprocess.run(
        ["opencode", "run", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"❌ ERROR:\n{result.stderr}"

    return result.stdout.strip()


# -------------------------
# MAIN EXECUTOR FUNCTION
# -------------------------

def run_agent(agent_name: str, user_text: str) -> str:
    prompt = load_prompt(agent_name, user_text)
    return run_opencode(prompt)