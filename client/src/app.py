import flet as ft
import threading
import time
from datetime import datetime
from ui.components.DropdownMenu.DropdownMenu import DropdownMenu
from tracker.Tracker import Window  # Assuming this is your Window class
from api.API import API
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
        active_app_title: str = Window.get_active_app()
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
            time_tree = API.get_total_spent_time()
            for title, title_data in time_tree.items():
                print("title, title_data:", title, title_data, sep="\n")

                dropdown_menu = DropdownMenu(title=title, session=title_data)
                self.ui.apps_info.controls.append(dropdown_menu.content)
 
            # Update counter and print response
            self.count_time = datetime.now().replace(microsecond=0)

        if self.titles_list[-1] != active_app_title:

            # Add a new app's title to the ui and list for condition rendering

            # Send session data to the server
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=self.titles_list[-1],
            )
            # for title, title_data in res.items():
            #     dropdown_menu = DropdownMenu(title=title, session=title_data)
            
            # self.ui.apps_info.controls.append(dropdown_menu.content)

            self.titles_list.append(active_app_title)
            # Update counter and update response
            self.count_time = datetime.now().replace(microsecond=0)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    tracker.start_tracking()
    # Initialize the menu data structure

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
