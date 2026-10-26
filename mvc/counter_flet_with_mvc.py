import flet as ft

from model import Model
from controller import Controller
from view import View


def main(page : ft.Page):
    model = Model()
    view = View(page)
    controller = Controller(model, view)

    view.set_controller(controller) # Serve per passare alla view il controller

ft.run(main)