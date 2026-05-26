import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    return result.stdout


def git_add(path="."):
    return run(f"git add {path}")


def git_commit(message):
    return run(f'git commit -m "{message}"')


def git_push():
    return run("git push")


def safe_git_pipeline(message):
    print("→ staging changes...")
    git_add("docs/")
    
    print("→ committing...")
    git_commit(message)
    
    print("→ pushing...")
    git_push()
    
    print("DONE")