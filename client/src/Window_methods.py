import flet as ft
import threading
import time

from imports import ActivityTrackerUI, ActivityTracker


class Window_methods(ActivityTracker):
    def __init__(self, page: ft.Page, ui: ActivityTrackerUI):
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
