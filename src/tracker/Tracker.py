import win32gui

class Window:  
  def get_active_window_title():
    window_handle = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window_handle)
    return title

  