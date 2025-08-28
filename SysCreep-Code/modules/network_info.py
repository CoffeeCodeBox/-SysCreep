import platform
import subprocess
from config import msg

def collect_network_info():
    try:
        with open("logs/network.txt", "w", encoding="utf-8") as f:
            system = platform.system()
            if system == "Windows":
                result = subprocess.check_output("ipconfig /all", shell=True, encoding="utf-8")
            elif system == "Linux":
                result = subprocess.check_output("ifconfig && cat /etc/resolv.conf", shell=True, encoding="utf-8")
            else:
                result = "Unsupported OS"
            f.write(result)
    except Exception as e:
        print(f"{msg('error')} [Network] {e}")