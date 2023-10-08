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
            Window.size = (930, 810)

        else:
            sistema_windows = False


    def run(self):
        # Coloque aqui o código que deseja executar na função run.
        menu_start = MenuStart()
        menu_sex = MenuSex()
        exibir_resultados = ExibirResultados()