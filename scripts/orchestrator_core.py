from scripts.state import load_state, save_state
from scripts.queue import pop_task
from scripts.git_ops import safe_git_pipeline


def run_pipeline(task: str):

    state = load_state()

    if state["running"]:
        return "⏳ Уже выполняется задача"

    state["running"] = True
    state["current_task"] = task
    save_state(state)

    try:
        # -------------------------
        # 1. SIMULATION OF AGENTS
        # -------------------------

        import subprocess

        def run_agent(agent, prompt):
            cmd = f'opencode run --agent {agent} "{prompt}"'

            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )

    return result.stdout

        # здесь у тебя позже будет:
        # architect → creative → ml → dl → validator

        # -------------------------
        # 2. GIT COMMIT STAGE
        # -------------------------

        #safe_git_pipeline(f"auto: {task}")

        state["last_result"] = result

        return result

    except Exception as e:
        return f"❌ Ошибка: {str(e)}"

    finally:
        state["running"] = False
        save_state(state)


def tick_queue():
    """Можно запускать периодически"""
    task = pop_task()
    if not task:
        return None
    return run_pipeline(task)