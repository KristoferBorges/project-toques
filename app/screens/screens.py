import platform
import random
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty

# Verifica se o usuário está usando Windows
if platform.system() == "Windows":
    sistema_windows = True
    font_column = 18
    font_row = 16
    font_button = 35
    font_text = 35
    font_text_menu = 48
    font_title = 60

else:
    sistema_windows = False
    font_column = 20
    font_row = 19
    font_button = 55
    font_text = 40
    font_text_menu = 60
    font_title = 80


class MenuStart(Screen):
    """
    Botão de iniciar o jogo.
    """
    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)


class SharedData:
    sexo = None


class MenuSex(Screen):
    """
    Menu com as opções de sexo, Masculino, Feminino e aleatório.
    """
    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)

    def definitionOfSexMen(self):
        self.sexo = 'Masculino'
        SharedData.sexo = self.sexo
    
    
    def definitionOfSexWomen(self):
        self.sexo = 'Feminino'
        SharedData.sexo = self.sexo
    

    def definitionOfSexRandom(self):
        listOfSex = ['Masculino', 'Feminino']
        self.sexo = random.choice(listOfSex)
        SharedData.sexo = self.sexo

class ExibirResultados(Screen):
    """
    Menu com os resultados das variantes.
    """

    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)

    def definitionOfRounds(self):
        rounds = random.randint(1, 3)
        return rounds


    def definitionOfTime(self):
        time = random.randint(10, 40)
        return time


    def clearLabel(self):
        self.ids.label_sexo.text = ''
        self.ids.label_result.text = ''


    def whatToDo(self):
        listOfRounds = {}
        listOfOptions = ['Beijos', 'Mordidas-Coxa', 'Mordidas-Bunda', 'Chupões', 'Chupões-X', 'Lambidas-Pescoço', 'Lambidas', 'Roçar']
        rounds = self.definitionOfRounds()
        
        for round in range(rounds):
            time = self.definitionOfTime()
            round = random.choice(listOfOptions)
            listOfRounds[round] = time
        print(SharedData.sexo)
        print(listOfRounds)

        formatted_text = "\n".join([f"{key}: {value} Segundos" for key, value in listOfRounds.items()])

        self.ids.label_sexo.text = SharedData.sexo
        self.ids.label_result.text = formatted_text
        return listOfRounds
    