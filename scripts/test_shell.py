import subprocess

print(subprocess.run(["powershell", "-Command", "echo OK"], capture_output=True, text=True))