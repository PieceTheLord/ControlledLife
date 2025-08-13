import flet as ft
import threading
import time
import app

class Window_methods(app.ActivityTracker):
    def __init__(self, page: ft.Page, tracker: app.ActivityTracker):
        self.tracker = tracker

    def start_tracking(self):
        thread = threading.Thread(target=self.update_timer, daemon=True)
        thread.start()

    def update_timer(self):
        time.sleep(0.001)
        while True:
            time.sleep(1)
            try:
                print(self.tracker.lv.controls)
            except Exception as e:
                print("Occured an errro ->", e)