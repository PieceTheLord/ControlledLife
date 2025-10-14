import flet as ft
from .lastDropdowMenu import lastDropdownMenu


class SubdropdownMenu:
    def __init__(self, session: dict):
        self.states = {
            "subtitle_expanded": False,
        }
        self.content_controls = [
            ft.Row([ft.Text(f"Total spent time - {session['total_spent_time']}")]),
        ]
        for subtitle, subtitle_data in session["subtitles"].items():
            # print(
            #     f"subtitle",
            #     subtitle,
            #     "subtitle_data",
            #     subtitle_data,
            #     sep="\n",
            # )
            self.content_controls.append(
                lastDropdownMenu(
                    title=subtitle,
                    session=subtitle_data,
                ).content
            )

        self.content = ft.Column(self.content_controls)
