import platform
import os

def generate_terminal_script():
    system = platform.system()
    if system == "Windows":
        with open("run_tool.bat", "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write("python main.py\n")
            f.write("pause\n")
    elif system == "Linux":
        with open("run_tool.sh", "w", encoding="utf-8") as f:
            f.write("#!/bin/bash\n")
            f.write("python3 main.py\n")
        os.chmod("run_tool.sh", 0o755)