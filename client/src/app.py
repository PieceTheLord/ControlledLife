import flet as ft
import threading
import time
from datetime import datetime
from tracker.Tracker import Window  # Assuming this is your Window class
import Window_methods
from utils.time_divider import time_split

class ActivityTrackertUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Activity tracker"
        self.lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
        self.page.add(self.lv)

    def add_title(self, title: str, time_elapsed: str):
        self.ui.lv.controls.append(ft.Text(f"{title} {time_elapsed}"))
        self.page.update()


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
            current_time = time_split(self.count_time)
            self.titles_list.append(active_app_title)
            self.ui.lv.controls.append(ft.Text(f"{active_app_title} {current_time}"))
            self.count_time = datetime.now()
        elif self.titles_list[-1] != active_app_title:
            current_time = time_split(self.count_time)
            self.ui.lv.controls.append(ft.Text(f"{self.titles_list[-1]} {current_time}"))
            self.titles_list.append(active_app_title)
            self.count_time = datetime.now()
            print("Origin:", self.ui.lv.controls)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    test = Window_methods.Window_methods(page, ui)
    tracker.start_tracking()
    test.start_tracking()


if __name__ == "__main__":
    ft.app(target=main)
