import flet as ft

class ActivityTrackerUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Activity tracker"
        self.lv = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
        self.page.add(self.lv)

    def add_title(self, title: str, time_elapsed: str):
        self.ui.lv.controls.append(ft.Text(f"{title} {time_elapsed}"))
        self.page.update()
