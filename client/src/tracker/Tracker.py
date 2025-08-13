import win32gui

class Window:  
  def get_active_app():
    """Get active app's title"""
    window_handle = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window_handle) 
    return title
  
  # def insert_active_title(title: str):
  #   last_wTitle = Db.get_last_wTitle()
  #   print(last_wTitle, title)


w = Window()

# w.insert_active_title()