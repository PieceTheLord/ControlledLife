import flet as ft


class lastDropdownMenu:
    def __init__(self, title, session: dict):
        self.states = {
            "subtitle_expanded": False,
        }
        self.session = session
        self.lastTitle_button = ft.IconButton(
            icon=(
                ft.Icons.ARROW_UPWARD_SHARP
                if self.states["subtitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            ),
            on_click=self.toggle_lastTitle,
        )
        self.last_title = ft.Text(title)
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        self.lastTitle_button,
                        self.last_title,
                    ]
                ),
                (
                    ft.Column(
                        [
                            ft.Text(f"{subtitle} - {subtitle_data['total_spent_time']}")
                            for subtitle, subtitle_data in session["subtitles"].items()
                        ]
                    )
                    if self.states["subtitle_expanded"]
                    else ft.Column([])
                ),
            ]
        )

    def toggle_lastTitle(self, e):
        self.states["subtitle_expanded"] = not self.states["subtitle_expanded"]
        print(self.states["subtitle_expanded"])
        self.lastTitle_button.icon = (
            ft.Icons.ARROW_UPWARD_SHARP
            if self.states["subtitle_expanded"]
            else ft.Icons.ARROW_DOWNWARD_SHARP
        )
        self.content.controls = [
            ft.Row(
                [
                    self.lastTitle_button,
                    self.last_title,
                ]
            ),
            (
                ft.Column(
                    [
                        ft.Text(f"{subtitle} - {subtitle_data['total_spent_time']}")
                        for subtitle, subtitle_data in self.session["subtitles"].items()
                    ]
                )
                if self.states["subtitle_expanded"]
                else ft.Column([])
            ),
        ]
