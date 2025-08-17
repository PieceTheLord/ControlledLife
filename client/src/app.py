import flet as ft
import threading
import time
from datetime import datetime
from tracker.Tracker import Window  # Assuming this is your Window class
import Window_methods
from ui.ActivityTrackerUI import ActivityTrackertUI
from api.API import API

class ActivityTracker:
    def __init__(self, page: ft.Page, ui: ActivityTrackertUI):
        self.page = page
        self.ui = ui
        self.count_time = datetime.now()
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
            self.titles_list.append(active_app_title)
            self.ui.lv.controls.append(ft.Text(f"{active_app_title} {self.count_time}"))
            self.count_time = datetime.now()
            res = API.insert_session_info(self.count_time, active_app_title)
            print(res)

        elif self.titles_list[-1] != active_app_title:
            self.ui.lv.controls.append(ft.Text(f"{self.titles_list[-1]} {self.count_time}"))
            self.titles_list.append(active_app_title)
            self.count_time = datetime.now()
            res = API.insert_session_info(self.count_time, active_app_title)
            print(res)
            # print("Origin:", self.ui.lv.controls)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    tracker.start_tracking()

    # test class-decmoposition code block
    # test = Window_methods.Window_methods(page, ui)
    # test.start_tracking()


if __name__ == "__main__":
    ft.app(target=main)