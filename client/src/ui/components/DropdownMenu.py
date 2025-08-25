import flet as ft
from api.API import API


class DropdownMenu:
    def __init__(self, session):
        self.states = {
            "mainTitle_expanded": False,
            "subtitle_expanded": False,
            "lastTitle_expanded": False,
        }
        self.menu_data = session

        self.mainTitleButton = ft.IconButton(
            icon=(
                ft.Icons.ARROW_UPWARD_SHARP
                if self.states["mainTitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            ),
            on_click=self.toggle_mainTitle,
        )
        self.subtitleButton = ft.IconButton(
            icon_size=18,
            icon=(
                ft.Icons.ARROW_UPWARD_SHARP
                if self.states["mainTitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            ),
            on_click=self.toggle_subtitle,
        )

        self.mainTtle = ft.Row(
            [
                self.mainTitleButton,
                ft.Row([ft.Text(self.menu_data["mainTitle"])]),
            ]
        )
        self.lastTitle = (
            ft.Row(
                spacing=ft.padding.only(left=100),
                controls=(
                    (
                        [
                            ft.Text(self.menu_data["subtitle1"]["subtitle2"]["title"]),
                        ]
                    ),
                ),
            )
            if self.states["subtitle_expanded"]
            else ft.Row([])
        )
        self.subtitle = (
            ft.Row(
                spacing=ft.padding.only(left=100),
                controls=[
                    self.subtitleButton,
                    ft.Text(self.menu_data["subtitle1"]["title"]),
                ],
            )
            if self.states["mainTitle_expanded"]
            else ft.Row([])
        )
        self.content = ft.Row(
            [
                ft.Column([self.mainTtle, self.subtitle, self.lastTitle]),
            ]
        )

    def check_mainTitle(self):
        if self.menu_data["subtitle1"]["title"] != "":
            return True

    def check_subtitle(self):
        if self.menu_data["subtitle1"]["subtitle2"]["title"] != "":
            return True

    def toggle_mainTitle(self, e):
        if self.check_mainTitle():
            self.states["mainTitle_expanded"] = not self.states["mainTitle_expanded"]
        self.mainTitleButton.icon = (
            ft.Icons.ARROW_UPWARD_SHARP
            if self.states["mainTitle_expanded"]
            else ft.Icons.ARROW_DOWNWARD_SHARP
        )
        self.subtitle.controls = [
            (
                ft.Row(
                    spacing=ft.padding.only(left=40),
                    controls=(
                        [
                            self.subtitleButton,
                            ft.Text(self.menu_data["subtitle1"]["title"]),
                        ]
                    ),
                )
                if self.states["mainTitle_expanded"]
                else ft.Row([])
            )
        ]

        self.update_menu()

    def toggle_subtitle(self, e):
        if self.check_subtitle():
            self.states["subtitle_expanded"] = not self.states["subtitle_expanded"]
        print(
            self.states["subtitle_expanded"],
            self.menu_data["subtitle1"]["subtitle2"]["title"],
        )
        self.subtitleButton.icon = (
            ft.Icons.ARROW_UPWARD_SHARP
            if self.states["subtitle_expanded"]
            else ft.Icons.ARROW_DOWNWARD_SHARP
        )
        self.lastTitle.controls = [
            (
                ft.Row(
                    [ft.Text(self.menu_data["subtitle1"]["subtitle2"]["title"])]
                )
                if self.states["subtitle_expanded"]
                else ft.Row([])
            )
        ]
        self.update_menu()

    def update_menu(self):

        self.content.update()
