import flet as ft
import time
import threading

from tracker.Tracker import Window

def main(page: ft.Page):
    page.title = "Infinite Timer"

    timer_running = True
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)

    def update_timer():
        while timer_running:
            time.sleep(1)
            lv.controls.append(ft.Text(Window.get_active_title()))
            page.update()

    def on_disconnect():
        nonlocal timer_running
        timer_running = False

    page.add(lv)
    page.on_disconnect = on_disconnect

    timer_thread = threading.Thread(target=update_timer, daemon=True)
    timer_thread.start()

    page.update()

if __name__ == "__main__":
    ft.app(target=main)