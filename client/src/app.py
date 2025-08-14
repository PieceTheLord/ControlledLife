import flet as ft

from imports import ActivityTrackerUI, ActivityTracker, Window_methods

def app(page: ft.Page):
    """Start the app, just for a beauty @main func"""
    ui = ActivityTrackerUI(page)
    tracker = ActivityTracker(page, ui)
    test = Window_methods(page, ui)
    tracker.ActivityTracker.start_tracking()
    test.start_tracking()
