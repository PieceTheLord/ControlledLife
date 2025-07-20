import flet as ft
import threading
import time
from datetime import datetime
from tracker.Tracker import Window  # Assuming this is your Window class
from utils.time_divider import parse_string  # Assuming this is your utility




class ActivityTracker:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Activity tracker"
        self.lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
        self.page.add(self.lv)
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
        active_app_title = Window.get_active_title()
        if not self.lv.controls:  # Check if list is empty
            current_time = str(datetime.now() - self.count_time).split(".")[0]
            self.titles_list.append(active_app_title)
            self.lv.controls.append(ft.Text(f"{active_app_title} {current_time}"))
            self.count_time = datetime.now()
        elif self.titles_list[-1] != active_app_title:
            current_time = str(datetime.now() - self.count_time).split(".")[0]
            self.lv.controls.append(ft.Text(f"{self.titles_list[-1]} {current_time}"))
            self.titles_list.append(active_app_title)
            self.count_time = datetime.now()
            print("Origin:", self.lv.controls)


def main(page: ft.Page):
    tracker = ActivityTracker(page)
    test = Window_methods(page, tracker)
    tracker.start_tracking()
    test.start_tracking()


class Window_methods(ActivityTracker):
    def __init__(self, page: ft.Page, tracker: ActivityTracker):
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
            



if __name__ == "__main__":
    ft.app(target=main)
