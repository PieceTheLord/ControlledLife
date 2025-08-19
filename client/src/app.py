import flet as ft
import threading
import time
from datetime import datetime
from tracker.Tracker import Window  # Assuming this is your Window class
from api.API import API
import Window_methods
from ui.ActivityTrackerUI import ActivityTrackertUI


class ActivityTracker:
    def __init__(self, page: ft.Page, ui: ActivityTrackertUI):
        self.page = page
        self.ui = ui
        self.count_time = datetime.now().replace(microsecond=0)
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

        # Check if list is empty
        if not self.ui.lv.controls:
            # Add a new app's title to ui and list for condition rendering
            self.titles_list.append(active_app_title)
            self.ui.lv.controls.append(
                ft.Text(
                    f"{active_app_title} {datetime.now() - self.count_time.replace(microsecond=0)}"
                )
            )
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=active_app_title,
            )

            # Update counter and print response
            self.count_time = datetime.now().replace(microsecond=0)
            print(res)

        elif self.titles_list[-1] != active_app_title:

            # Add a new app's title to the ui and list for condition rendering
            self.ui.lv.controls.append(
                ft.Text(
                    f"{self.titles_list[-1]} {datetime.now().replace(microsecond=0) - self.count_time}"
                )
            )
            self.titles_list.append(active_app_title)
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=active_app_title,
            )

            # Update counter and update response
            self.count_time = datetime.now().replace(microsecond=0)
            print(res)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    test = Window_methods.Window_methods(page, tracker)
    tracker.start_tracking()

    # test class-decmoposition code block
    # test = Window_methods.Window_methods(page, ui)
    # test.start_tracking()


if __name__ == "__main__":
    ft.app(target=main)
