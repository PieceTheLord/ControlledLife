import flet_timer.flet_timer
from tracker.Tracker import Window

import flet as ft


def main(page: ft.Page):
    lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
    ref = ft.Ref
    page.title = "Title"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Create the list of our tracking apps' title

    

    # function to get the windows' title
    def show_window_title():
        last_title = Window.get_active_title()
        # if (last_title == Window.get_active_title()):
        lv.controls.append(ft.Text(last_title))
        # else:
        #     pass
        # re-render the app, because of its SPA
        page.update()
    
    def on_connect():
        print("App connected")

    page.on_connect = on_connect
    
    # add the timer to recall the @get_window_title func every second
    
    timer = flet_timer.flet_timer.Timer("timer", 1, show_window_title)
    page.add(timer, lv)
    

ft.app(main)

if __name__ == "__main__":
    main()
