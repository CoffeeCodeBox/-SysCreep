import time
import platform
from datetime import datetime
import os
from config import msg

def capture_screen_loop(duration=600, interval=1):
    try:
        system = platform.system()
        if system == "Windows" or system == "Darwin":
            from PIL import ImageGrab
            grab = ImageGrab.grab
        elif system == "Linux":
            import pyautogui
            grab = pyautogui.screenshot
        else:
            print("Unsupported OS for screenshots")
            return

        end_time = time.time() + duration
        while time.time() < end_time:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            img = grab()
            img.save(f"logs/screenshots/screen_{timestamp}.png")
            time.sleep(interval)
    except Exception as e:
        print(f"{msg('error')} [Screenshot] {e}")