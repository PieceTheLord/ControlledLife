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
            print(
                f"subtitle",
                subtitle,
                "subtitle_data",
                subtitle_data,
                sep="\n",
            )
            self.content_controls.append(
                lastDropdownMenu(
                    session=subtitle_data,
                    subtitle_expanded=self.states["subtitle_expanded"],
                ).content
            )
            if subtitle_data["subtitles"]:
                for subtitle2, subtitle2_data in subtitle_data["subtitles"].items():
                    print(
                        "subtitle2",
                        subtitle2,
                        "subtitle2_data",
                        subtitle2_data,
                        sep="\n",
                    )

        self.content = ft.Column(self.content_controls)
