import flet as ft


class SubdropdownMenu:
    def __init__(self, mainTitle_expanded):
        pass



    #     self.states = {
    #         "subtitle_expanded": False,
    #         "lastTitle_expanded": False,
    #         "mainTitle_expanded": mainTitle_expanded,
    #     }
    #     self.menu_data = {"subtitle1"}
    #     self.subtitleButton = ft.IconButton(
    #         icon_size=18,
    #         icon=(
    #             ft.Icons.ARROW_UPWARD_SHARP
    #             if self.states["mainTitle_expanded"]
    #             else ft.Icons.ARROW_DOWNWARD_SHARP
    #         ),
    #         on_click=self.toggle_subtitle,
    #     )
    #     self.lastTitle = (
    #         ft.Row(
    #             [
    #                 ft.Text(self.menu_data["subtitle1"]["subtitle2"]["title"]),
    #             ]
    #         )
    #         if self.states["subtitle_expanded"]
    #         else ft.Row([])
    #     )
    #     self.subtitle = (
    #         ft.Row(
    #             [
    #                 self.subtitleButton,
    #                 ft.Text(self.menu_data["subtitle1"]["title"]),
    #             ],
    #         )
    #         if self.states["mainTitle_expanded"]
    #         else ft.Row([])
    #     )
    #     self.content = ft.Column(
    #         [ft.Row([self.subtitleButton, self.subtitle]), self.lastTitle]
    #     )

    # def check_subtitle(self):
    #     if self.menu_data["subtitle1"]["subtitle2"]["title"] != "":
    #         return True