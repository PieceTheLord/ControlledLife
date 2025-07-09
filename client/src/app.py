import time
from tracker.Tracker import Window
import threading
import flet as ft


def main(page: ft.Page):

    # Create the list of our tracking apps' title
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
    page.title = "Activity tracker"
    timer_running = True
    

    def update_timer():
        while timer_running:
            time.sleep(1)
            add_active_window_title()
            page.update()

    def add_active_window_title():
        lv.controls.append(ft.Text(Window.get_active_title()))

    page.add(lv)

    timer_thread = threading.Thread(target=update_timer, daemon=True)
    timer_thread.start()


    page.update()
    


if __name__ == "__main__":
    ft.app(target=main)
