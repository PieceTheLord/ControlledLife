import flet as ft


class State:
    toggle = True


s = State()


class ActivityTrackertUI:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Activity tracker"
        self.apps_info = ft.ListView(expand=1, padding=20, spacing=10, auto_scroll=True)
        self.page.add(self.apps_info)
        self.add_chart()

    def add_title(self, title: str, time_elapsed: str):
        self.ui.apps_info.controls.append(ft.Text(f"{title} {time_elapsed}"))
        self.self.page.update()

        mainTitleButton = ft.IconButton(
            icon=(
                ft.Icons.ARROW_UPWARD_SHARP
                if states["mainTitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            ),
            on_click=toggle_mainTitle,
        )

        content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                mainTitleButton,
                                ft.Row([ft.Text(menu_data["mainTitle"])]),
                            ]
                        )
                    ]
                ),
            ]
        )

        def update_menu():
            mainTitleButton.icon = (
                ft.Icons.ARROW_UPWARD_SHARP
                if states["mainTitle_expanded"]
                else ft.Icons.ARROW_DOWNWARD_SHARP
            )
            content.update()

        page.add(content)
        update_menu()

    # Line Chart #TODO: This is needs to be done
    def add_chart(self):
        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=8,
                color=ft.Colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.PINK,
                below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 3),
                    ft.LineChartDataPoint(10, 1.3),
                    ft.LineChartDataPoint(13, 2.5),
                ],
                color=ft.Colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        data_2 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 4),
                    ft.LineChartDataPoint(5, 1.8),
                    ft.LineChartDataPoint(7, 5),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=4,
                color=ft.Colors.with_opacity(0.5, ft.Colors.LIGHT_GREEN),
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.with_opacity(0.5, ft.Colors.PINK),
                below_line_bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.PINK),
                stroke_width=4,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 3.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 5),
                    ft.LineChartDataPoint(10, 3.3),
                    ft.LineChartDataPoint(13, 4.5),
                ],
                color=ft.Colors.with_opacity(0.5, ft.Colors.CYAN),
                stroke_width=4,
                stroke_cap_round=True,
            ),
        ]

        chart = ft.LineChart(
            data_series=data_1,
            border=ft.Border(
                bottom=ft.BorderSide(
                    4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)
                )
            ),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                ],
                labels_size=40,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "SEP",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=7,
                        label=ft.Container(
                            ft.Text(
                                "OCT",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=12,
                        label=ft.Container(
                            ft.Text(
                                "DEC",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY),
            min_y=0,
            max_y=4,
            min_x=0,
            max_x=14,
            # animate=5000,
            expand=True,
        )

        def toggle_data(e):
            if s.toggle:
                chart.data_series = data_2
                chart.data_series[2].point = True
                chart.max_y = 6
                chart.interactive = False
            else:
                chart.data_series = data_1
                chart.max_y = 4
                chart.interactive = True
            s.toggle = not s.toggle
            chart.update()

        # self.page.add(ft.IconButton(ft.Icons.REFRESH, on_click=toggle_data), chart)
