from datetime import datetime
import time
from tracker.Tracker import Window
import threading
import flet as ft

def main(page: ft.Page):

    # Create the list of our tracking apps' title
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
    page.title = "Activity tracker"
    timer_running = True
    count_time = datetime.now()


    def update_timer():
        while timer_running:
            time.sleep(1)
            add_active_window_title()
            page.update()

    def add_active_window_title():
        nonlocal count_time
        app_title = Window.get_active_title()
        if (len(lv.controls) == 0):
            current_time = datetime.now() - count_time
            lv.controls.append(ft.Text(app_title))   
            print(app_title, current_time)
            count_time = datetime.now()
        elif (lv.controls[-1].value != app_title):
            current_time = datetime.now() - count_time
            lv.controls.append(ft.Text(app_title))
            print(lv.controls[-2].value, current_time)
            count_time = datetime.now()
        else:
            pass
        
    page.add(lv)

    timer_thread = threading.Thread(target=update_timer, daemon=True)
    timer_thread.start()

    page.update()
    

if __name__ == "__main__":
    ft.app(target=main)
