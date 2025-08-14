import flet as ft

from app import app


def main(page: ft.Page):
    app(page)


if __name__ == "__main__":
    ft.app(target=main)
