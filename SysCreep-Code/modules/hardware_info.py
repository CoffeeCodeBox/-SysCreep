import platform
import psutil
from config import msg

def collect_hardware_info():
    try:
        with open("logs/hardware.txt", "w", encoding="utf-8") as f:
            f.write(f"System: {platform.system()} {platform.release()}\n")
            f.write(f"Version: {platform.version()}\n")
            f.write(f"Processor: {platform.processor()}\n")
            f.write(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n")
            f.write(f"Disk Usage: {psutil.disk_usage('/').percent}% used\n")
    except Exception as e:
        print(f"{msg('error')} [Hardware] {e}")