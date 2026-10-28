import os
import platform
import subprocess

print("=== Process Information ===")
print("Process ID:", os.getpid())
print("Parent Process ID:", os.getppid())
print("Hostname:", platform.node())

print("\n=== Current Processes ===")
result = subprocess.run(
    ["ps", "-eo", "pid,ppid,comm"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout)
