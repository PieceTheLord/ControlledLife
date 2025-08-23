import flet as ft
import threading
import time
from datetime import datetime
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

            self.ui.lv.controls.append(
                ft.Text(
                    f"{active_app_title} {datetime.now().replace(microsecond=0) - self.count_time}"
                )
            )
            # Update counter and print response
            self.count_time = datetime.now().replace(microsecond=0)
            print(res)

        if self.titles_list[-1] != active_app_title:

            # Add a new app's title to the ui and list for condition rendering
            self.ui.lv.controls.append(
                ft.Text(
                    f"{self.titles_list[-1]} {datetime.now().replace(microsecond=0) - self.count_time}"
                )
            )

            # Send session data to the server
            res = API.insert_session_info(
                spentTime=datetime.now().replace(microsecond=0) - self.count_time,
                startTime=self.count_time,
                endTime=datetime.now().replace(microsecond=0),
                title=self.titles_list[-1],
            )
            self.titles_list.append(active_app_title)

            # Update counter and update response
            self.count_time = datetime.now().replace(microsecond=0)
            print(res)


def main(page: ft.Page):
    ui = ActivityTrackertUI(page)
    tracker = ActivityTracker(page, ui)
    tracker.start_tracking()

    mainTitle_expanded = False
    subtitle_expanded = False

    def toggle_mainTitle(e):
        nonlocal mainTitle_expanded
        mainTitle_expanded = not mainTitle_expanded
        update_menu()

    def toggle_subtitle(e):
        nonlocal subtitle_expanded
        subtitle_expanded = not subtitle_expanded
        update_menu()

    # Initialize the menu data structure
    menu_data = API.get_last_session()  # Corrected initialization
    print("menu_data ->", menu_data)
    # Expansion states dictionary
    expanded_states = {}

    def toggle_main_title(mainTitles):
        def f(e):
            expanded_states[mainTitles] = not expanded_states[mainTitles]
            update_menu()

        return f

    def toggle_subtitle(main_title, subtitle):
        def f(e):
            if main_title not in expanded_states:
                return  # Or handle this case appropriately

            if "subtitles" not in expanded_states[main_title]:
                return

            if subtitle not in expanded_states[main_title]["subtitles"]:
                return

            expanded_states[main_title]["subtitles"][subtitle] = not expanded_states[
                main_title
            ]["subtitles"][subtitle]
            update_menu()

        return f

    def update_menu_data():
        nonlocal menu_data
        # Initialize expanded states
        # expanded_states.clear()
        for mainTitles in menu_data.keys():
            expanded_states[mainTitles] = {"expanded": False, "subtitles": {}}
            for subtitle in menu_data[mainTitles].keys():
                expanded_states[mainTitles]["subtitles"][subtitle] = False

    def build_menu_items():
        menu_items = []
        for mainTitles, subtitles in menu_data.items():
            # Main title row
            menu_items.append(
                ft.Row(
                    [
                        ft.IconButton(
                            icon=(
                                ft.Icons.KEYBOARD_ARROW_DOWN
                                if mainTitles not in expanded_states
                                or not expanded_states[mainTitles]["expanded"]
                                else ft.Icons.KEYBOARD_ARROW_UP
                            ),
                            on_click=toggle_main_title(mainTitles),
                        ),
                        ft.Text(mainTitles),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

            # Subtitle rows
            if (
                mainTitles in expanded_states
                and expanded_states[mainTitles]["expanded"]
            ):
                for subtitle, details in subtitles.items():
                    menu_items.append(
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=(
                                        ft.Icons.KEYBOARD_ARROW_DOWN
                                        if mainTitles not in expanded_states
                                        or "subtitles"
                                        not in expanded_states[mainTitles]
                                        or subtitle
                                        not in expanded_states[mainTitles]["subtitles"]
                                        or not expanded_states[mainTitles]["subtitles"][
                                            subtitle
                                        ]
                                        else ft.Icons.KEYBOARD_ARROW_UP
                                    ),
                                    on_click=toggle_subtitle(mainTitles, subtitle),
                                ),
                                ft.Text(f"  {subtitle}"),
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    )
                    # Displaying details for subtitle
                    if (
                        mainTitles in expanded_states
                        and "subtitles" in expanded_states[mainTitles]
                        and subtitle in expanded_states[mainTitles]["subtitles"]
                        and expanded_states[mainTitles]["subtitles"][subtitle]
                    ):
                        for detail in details:
                            menu_items.append(
                                ft.Container(
                                    content=ft.Text(
                                        f"    {detail['subtitle2']} - Start: {detail['startTime']}, End: {detail['endTime']}, Spent: {detail['spentTime']}"
                                    ),
                                    padding=ft.padding.only(left=40),
                                )
                            )

        return menu_items

    def update_menu():
        update_menu_data()  # Call this before building menu items
        # page.controls.clear()
        page.add(ft.Column(controls=build_menu_items()))

    update_menu()  # Initial menu build

    # test class-decmoposition code block
    # test = Window_methods.Window_methods(page, ui)
    # test.start_tracking()


if __name__ == "__main__":
    ft.app(target=main)
