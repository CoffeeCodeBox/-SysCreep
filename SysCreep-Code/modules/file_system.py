import os
import platform
from config import msg

def list_drives_and_files():
    try:
        drives = []
        if os.name == "nt":
            import string
            from ctypes import windll
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(letter + ":\\")
                bitmask >>= 1
        else:
            drives = ["/", "/home", "/mnt", "/media"]

        with open("logs/drives.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(drives))

        with open("logs/files_by_drive.txt", "w", encoding="utf-8") as f:
            for drive in drives:
                f.write(f"\n--- Files in {drive} ---\n")
                for root, dirs, files in os.walk(drive):
                    for name in files:
                        full_path = os.path.join(root, name)
                        f.write(full_path + "\n")
    except Exception as e:
        print(f"{msg('error')} [Drives/Files] {e}")