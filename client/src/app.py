import flet as ft
import threading
import time
from datetime import datetime
from tracker.Tracker import Window  # Assuming this is your Window class
from api.API import API
from ui.ActivityTrackerUI import ActivityTrackertUI
from ui.components.DropdownMenu import DropdownMenu


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
        if not self.titles_list:
            # Add a new app's title to ui and list for condition rendering
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=active_app_title,
            )
            self.titles_list.append(active_app_title)
            all_session = API.get_all_session()

            for i in range(len(all_session)):
                dropdown_menu = DropdownMenu(all_session[i])
                self.ui.apps_info.controls.append(dropdown_menu.content)
                
            # Update counter and print response
            self.count_time = datetime.now().replace(microsecond=0)
            print(res)

        if self.titles_list[-1] != active_app_title:

            # Add a new app's title to the ui and list for condition rendering

            # Send session data to the server
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=self.titles_list[-1],
            )
            dropdown_menu = DropdownMenu(res["data"])
            print(res)
            self.ui.apps_info.controls.append(dropdown_menu.content)

            self.titles_list.append(active_app_title)
            # Update counter and update response
            self.count_time = datetime.now().replace(microsecond=0)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    tracker.start_tracking()
    # Initialize the menu data structure

    menu_data = API.get_last_session()  # Corrected initialization
    print("menu_data ->", menu_data)
    # Expansion states dictionary
    print(menu_data, sep="\n")

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
