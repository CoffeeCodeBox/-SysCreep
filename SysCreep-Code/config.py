MESSAGES = {
    "setup": "Setting up environment...",
    "start": "Starting pentest tool...",
    "error": "Error occurred:",
    "keylog": "Logging keystrokes..."
}

def msg(key):
    return MESSAGES.get(key, "")