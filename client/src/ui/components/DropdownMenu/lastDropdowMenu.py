import flet as ft


class lastDropdownMenu:
    def __init__(self, subtitle_expanded, session):
        self.states = {
            "subtitle_expanded": subtitle_expanded,
        }
        self.content_controls = []
        self.content = ft.Column(
            [
                ft.Text(f"{subtitle} - {subtitle_data['total_spent_time']}")
                for subtitle, subtitle_data in session["subtitles"].items()
            ]
        )
