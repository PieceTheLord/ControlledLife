import flet_timer.flet_timer
import win32gui
import time
import flet as ft

def get_active_window_title():
    window_handle = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window_handle)
    return title

def main(page: ft.Page):
    page.title = "Title"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    txt_number = ft.Text(
        get_active_window_title(),
        text_align=ft.TextAlign.CENTER, 
        width=400
    )

    def get_window_title():
        txt_number.value = get_active_window_title(),
        page.update()


    page.add(
        ft.Row(
            [
                # ft.IconButton(icon=ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                # ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    timer = flet_timer.flet_timer.Timer("timer", 1, get_window_title)
    page.add(timer)
    

ft.app(main)

# while True:
# active_window_title = get_active_window_title()
# print(f"Active window title: {get_active_window_title()}")
# time.sleep(.5)
