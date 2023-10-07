import platform
from kivy.core.window import Window
from app.screens.screens import MenuStart
from app.screens.screens import MenuSex
from app.screens.screens import ExibirResultados

class Setup:
    def __init__(self):
        # Verifica se o usuário está usando Windows
        if platform.system() == "Windows":
            sistema_windows = True
            font_column = 18
            font_row = 16
            font_button = 35
            font_text = 35
            font_text_menu = 48
            font_title = 60
            Window.size = (1130, 810)

        else:
            sistema_windows = False
            font_column = 20
            font_row = 19
            font_button = 55
            font_text = 40
            font_text_menu = 60
            font_title = 80
        pass


    def run(self):
        # Coloque aqui o código que deseja executar na função run.
        menu_start = MenuStart()
        menu_sex = MenuSex()
        exibir_resultados = ExibirResultados()