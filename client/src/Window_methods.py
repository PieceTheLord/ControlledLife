import flet as ft
import threading
import time
from ui.ActivityTrackerUI import ActivityTrackertUI
import app


class Window_methods(app.ActivityTracker):
    def __init__(self, page: ft.Page, ui: ActivityTrackertUI):
        self.ui = ui

    def start_tracking(self):
        thread = threading.Thread(target=self.update_timer, daemon=True)
        thread.start()

    def update_timer(self):
        time.sleep(0.001)
        while True:
            time.sleep(1)
            try:
                print(self.ui.lv.controls)
            except Exception as e:
                print("Occured an errro ->", e)