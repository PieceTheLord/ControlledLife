import flet as ft
from api.API import API
from .SubdropdownMenu import SubdropdownMenu


class DropdownMenu:
    def __init__(self, title, session):

        self.states = {"mainTitle_expanded": False}
        self.title = title
        self.menu_data = session

        self.mainTitleButton = ft.IconButton(
            icon=(
                ft.Icons.ARROW_UPWARD_SHARP
                if self.states["mainTitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            ),
            on_click=self.toggle_mainTitle,
        )
        self.content = ft.Row([self.mainTitleButton, ft.Text(self.title)])

    def toggle_mainTitle(self, e):
        self.states["mainTitle_expanded"] = not self.states["mainTitle_expanded"]
        self.mainTitleButton.icon = (
            ft.Icons.ARROW_UPWARD_SHARP
            if self.states["mainTitle_expanded"]
            else ft.Icons.ARROW_DOWNWARD_SHARP
        )
        self.update_menu()

    #     self.states = {"mainTitle_expanded": False}
    #     self.menu_data = session

    #     self.mainTtle = ft.Row(
    #         [
    #             self.mainTitleButton,
    #             ft.Row([ft.Text(self.menu_data["mainTitle"])]),
    #         ]
    #     )
    #     self.details = SubdropdownMenu(
    #         mainTitle_expanded=self.states["mainTitle_expanded"]
    #     )
    #     self.content = ft.Row(
    #         [
    #             ft.Column([self.mainTtle, self.details.content]),
    #         ]
    #     )

    # # Check the subtitle exists
    # def check_mainTitle(self):
    #     if self.menu_data["subtitle1"]["title"] != "":
    #         return True
    #     self.update_menu()

    # # Check the last title existst (e.g app.py or a vieo's title)

    # def toggle_mainTitle(self, e):
    #     if self.states["mainTitle_expanded"] == True:
    #         self.states["mainTitle_expanded"] = False
    #         self.states["subtitle_expanded"] = False
    #     elif self.check_mainTitle():
    #         self.states["mainTitle_expanded"] = not self.states["mainTitle_expanded"]
    #     # Rebuild IconButton, because self.content update doesn't rebuild the page based on code
    #     self.mainTitleButton.icon = (
    #         ft.Icons.ARROW_UPWARD_SHARP
    #         if self.states["mainTitle_expanded"]
    #         else ft.Icons.ARROW_DOWNWARD_SHARP
    #     )

    #     # Rebuild the controls, because self.content update doesn't rebuild the page based on code
    #     self.details.subtitle.controls = [
    #         (
    #             ft.Row(
    #                 [
    #                     self.subtitleButton,
    #                     ft.Text(self.menu_data["subtitle1"]["title"]),
    #                 ]
    #             )
    #             if self.states["mainTitle_expanded"]
    #             else ft.Row([])
    #         )
    #     ]

    #     # Rebuild controls
    #     self.details.lastTitle.controls = [
    #         (
    #             ft.Row([ft.Text(self.menu_data["subtitle1"]["subtitle2"]["title"])])
    #             if self.states["subtitle_expanded"]
    #             else ft.Row([])
    #         )
    #     ]

    #     self.update_menu()

    # def toggle_subtitle(self, e):
    #     if self.check_subtitle():
    #         self.states["subtitle_expanded"] = not self.states["subtitle_expanded"]
    #     print(
    #         self.states["subtitle_expanded"],
    #         self.menu_data["subtitle1"]["subtitle2"]["title"],
    #     )
    #     # Rebuild IconButton
    #     self.subtitleButton.icon = (
    #         ft.Icons.ARROW_UPWARD_SHARP
    #         if self.states["subtitle_expanded"]
    #         else ft.Icons.ARROW_DOWNWARD_SHARP
    #     )
    #     # Rebuild last title control
    #     self.lastTitle.controls = [
    #         (
    #             ft.Row([ft.Text(self.menu_data["subtitle1"]["subtitle2"]["title"])])
    #             if self.states["subtitle_expanded"]
    #             else ft.Row([])
    #         )
    #     ]
    #     self.update_menu()

    def update_menu(self):

        self.content.update()
