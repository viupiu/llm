import subprocess

print(subprocess.run(["npx", "-v"], capture_output=True, text=True))