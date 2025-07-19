from datetime import datetime
import time
from tracker.Tracker import Window
import threading
import flet as ft
from utils.time_divider import parse_string


def main(page: ft.Page):

    # Create the list of our tracking apps' title
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
    page.title = "Activity tracker"
    timer_running = True
    count_time = datetime.now()
    titles_list: list[str] = []

    def update_timer():
        while timer_running:
            time.sleep(1)
            add_active_window_title()
            page.update()

    def add_active_window_title():
        nonlocal count_time
        active_app_title = Window.get_active_title()
        if len(lv.controls) == 0:
            current_time = str(datetime.now() - count_time).split(".")[0]
            titles_list.append(active_app_title)
            lv.controls.append(ft.Text(active_app_title + " " + current_time))

            count_time = datetime.now()

        elif titles_list[-1] != active_app_title:
            current_time = str(datetime.now() - count_time).split(".")[0]
            lv.controls.append(ft.Text(titles_list[-1] + " " + current_time))
            titles_list.append(active_app_title)

            count_time = datetime.now()
        else:
            pass

    page.add(lv)

    timer_thread = threading.Thread(target=update_timer, daemon=True)
    timer_thread.start()

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
