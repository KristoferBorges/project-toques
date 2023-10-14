import platform
from kivy.core.window import Window
from app.screens.screens import MenuStart
from app.screens.screens import MenuSex
from app.screens.screens import ExibirResultados
from app.screens.screens import DifficultyMode

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
        difficulty_mode = DifficultyMode()
        menu_sex = MenuSex()
        exibir_resultados = ExibirResultados()