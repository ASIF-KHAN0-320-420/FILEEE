import os
import subprocess

commands = [
    ["pkg", "install", "git", "python", "-y"],
    ["git", "clone", "https://github.com/walilila40-ui/FILEEE.git", "/sdcard/FILEEE"],
]

for command in commands:
    subprocess.run(command)

os.system("ls /sdcard/FILEEE")
