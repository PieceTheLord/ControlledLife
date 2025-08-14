import flet as ft
import threading
import time
import datetime

from imports import ActivityTrackerUI, utils, Window

class ActivityTracker:
    def __init__(self, page: ft.Page, ui: ActivityTrackerUI):
        self.page = page
        self.ui = ui
        self.count_time = datetime.datetime.now()
        self.titles_list = []

    def start_tracking(self):
        timer_thread = threading.Thread(target=self.update_timer, daemon=True)
        timer_thread.start()

    def update_timer(self):
        while True:
            time.sleep(1)
            self.add_active_window_title()

            self.page.update()

    def add_active_window_title(self):
        active_app_title: str = Window.get_active_title()
        if not self.ui.lv.controls:  # Check if list is empty
            current_time = utils.time_split(self.count_time)
            self.titles_list.append(active_app_title)
            self.ui.lv.controls.append(ft.Text(f"{active_app_title} {current_time}"))
            self.count_time = datetime.now()
        elif self.titles_list[-1] != active_app_title:
            current_time = utils.time_split(self.count_time)
            self.ui.lv.controls.append(
                ft.Text(f"{self.titles_list[-1]} {current_time}")
            )
            self.titles_list.append(active_app_title)
            self.count_time = datetime.now()
            print("Origin:", self.ui.lv.controls)
