import platform
import random
from pygame import mixer
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from app import sound_button, tuin, startGame

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

    def startButton(self):
        sound_button.play()


class SharedData:
    sexo = None
    start = None


class MenuSex(Screen):
    """
    --> Menu com as opções de sexo, Masculino, Feminino e aleatório.
    """
    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)

    def definitionOfSexMen(self):
        """
        --> Define o sexo como Masculino ao clicar no botão.
        """
        self.sexo = 'Masculino'
        SharedData.sexo = self.sexo
        sound_button.play()
    
    
    def definitionOfSexWomen(self):
        """
        --> Define o sexo como Feminino ao clicar no botão.
        """
        self.sexo = 'Feminino'
        SharedData.sexo = self.sexo
        sound_button.play()
    

    def definitionOfSexRandom(self):
        """
        --> Define o sexo como aleatório ao clicar no botão.
        """
        listOfSex = ['Masculino', 'Feminino']
        self.sexo = random.choice(listOfSex)
        SharedData.sexo = self.sexo
        sound_button.play()

class ExibirResultados(Screen):
    """
    --> Menu com os resultados das variantes.
    """
    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)

    def definitionOfRounds(self):
        """
        --> Define a quantidade de rounds.
        """
        rounds = random.randint(1, 3)
        return rounds


    def definitionOfTime(self):
        """
        --> Define o tempo de cada round.
        """
        time = random.randint(10, 40)
        return time


    def clearLabel(self):
        """
        --> Limpa os labels e altera a variável de start.
        """
        self.ids.label_sexo.text = ''
        self.ids.label_result.text = ''
        self.ids.button_comecar.background_color = 1, 0, 0, 1

        self.start = False
        SharedData.start = self.start
        sound_button.play()
        return SharedData.start
    

    def whatToDo(self):
        """
        --> Define o que será feito em cada round.
        """
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

        if SharedData.sexo == 'Feminino':
            self.ids.label_sexo.color = [1, 0.3, 0.3, 1]
            self.ids.label_sexo.text = SharedData.sexo
        else:
            self.ids.label_sexo.color = [0, 1, 1, 1]
            self.ids.label_sexo.text = SharedData.sexo
        self.ids.label_result.text = formatted_text

        self.start = True
        SharedData.start = self.start

        tuin.play()
        return listOfRounds, SharedData.start
    
    def changeColor(self):
        """
        --> Muda a cor do botão de vermelho para verde.
        """
        self.ids.button_comecar.background_color = [0, 1, 0, 1] 

    
    def startGame(self):
        """
        --> Inicia o jogo após gerar as informações.
        """
        if SharedData.start == True:
            startGame.play()
        else:
            pass
        