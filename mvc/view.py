# Nel pattern MVC, gestisce la parte di interfaccia grafica

import flet as ft

class View:
    def __init__(self, page : ft.Page): # Con i ":" si indica il tipo del parametro
        self._page = page
        self._controller = None # Prima la dichiaro

    def set_controller(self, controller):
        self._controller = controller # Poi la inizializzo con questa funzione
        self.inizializza_gui() # Va chiamata DOPO aver impostato il controller


    def inizializza_gui(self):
        self._page.window.width = 420
        self._page.window.height = 300
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER

        myBtnMinus = ft.IconButton(icon=ft.Icons.REMOVE,
                                   icon_size=20,
                                   on_click=self._controller.handler_minus, )
        myBtnPlus = ft.IconButton(icon=ft.Icons.ADD,
                                  icon_size=20,
                                  on_click=self._controller.handler_plus, )
        self._myText = ft.TextField(value=0,
                              width=100,
                              disabled=True,
                              text_size=20,
                              text_align=ft.TextAlign.CENTER,
                              )

        myRow = ft.Row([myBtnMinus, self._myText, myBtnPlus],
                       alignment=ft.MainAxisAlignment.CENTER, )

        self._page.controls.append(myRow)

    def aggiorna_gui(self, v):
        self._myText.value = v
        self._page.update()