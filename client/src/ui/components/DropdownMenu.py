import flet as ft
from ActivityTrackerUI import ActivityTrackertUI

class DropdownMenu:
    def __init__(self, page: ft.Page, ui: ActivityTrackertUI):
        self.ui = ui
        self.page = page
        
    def add_dropdown_meny(self):
        self.ui.apps_info.controls.append(ft.)