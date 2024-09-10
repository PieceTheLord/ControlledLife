import win32gui
import time

def get_active_window_title():
    window_handle = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window_handle)
    return title

while True:
    active_window_title = get_active_window_title()
    print(f"Active window title: {active_window_title}")
    time.sleep(.5)
