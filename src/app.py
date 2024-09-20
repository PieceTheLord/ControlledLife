import flet_timer.flet_timer
from tracker.Tracker import Window
from db.connection import conn
import time
import flet as ft



def main(page: ft.Page):
    ref = ft.Ref
    page.title = "Title"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Create the list of our tracking apps' title
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)

    # function to get the windows' title
    def show_window_title():
        lv.controls.append(ft.Text(Window.get_active_window_title()))
        # re-render the app, because of its SPA
        page.update()
    

    btn = ft.IconButton(icon=ft.icons.ADD, on_click=lambda e: page.add(ft.Text('Hi!')))
    
    page.add(lv, btn)
    
    # add the timer to recall the @get_window_title func every second
    timer = flet_timer.flet_timer.Timer("timer", 1, show_window_title)
    # page.add(timer)
    

ft.app(main)

# if __name__ == "__main__":
#     main()
