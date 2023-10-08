import platform
import random
from time import sleep
from pygame import mixer
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import NumericProperty
from app import click_button, tuin, startGame, back_button, finish_time

# Verifica se o usuário está usando Windows
if platform.system() == "Windows":
    sistema_windows = True
    font_start = 110
    font_column = 18
    font_row = 16
    font_button = 35
    font_text = 35
    font_text_menu = 48
    font_title = 60

    font_timing = 190
else:
    sistema_windows = False
    font_start = 135
    font_column = 20
    font_row = 19
    font_button = 65
    font_text = 40
    font_text_menu = 45
    font_title = 70

    font_timing = 190


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
    font_start = NumericProperty(font_start)
    font_timing = NumericProperty(font_timing)

    def startButton(self):
        click_button.play()


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
    font_start = NumericProperty(font_start)
    font_timing = NumericProperty(font_timing)

    def definitionOfSexMen(self):
        """
        --> Define o sexo como Masculino ao clicar no botão.
        """
        self.sexo = 'Masculino'
        SharedData.sexo = self.sexo
        click_button.play()
    
    
    def definitionOfSexWomen(self):
        """
        --> Define o sexo como Feminino ao clicar no botão.
        """
        self.sexo = 'Feminino'
        SharedData.sexo = self.sexo
        click_button.play()
    

    def definitionOfSexRandom(self):
        """
        --> Define o sexo como aleatório ao clicar no botão.
        """
        listOfSex = ['Masculino', 'Feminino']
        self.sexo = random.choice(listOfSex)
        SharedData.sexo = self.sexo
        click_button.play()

class ExibirResultados(Screen):
    """
    --> Menu com os resultados das variantes.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.listOfRounds = {}

    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)
    font_start = NumericProperty(font_start)
    font_timing = NumericProperty(font_timing)

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
        global total

        self.ids.label_sexo.text = ''
        self.ids.label_result_timing.text = ''
        self.ids.button_comecar.background_color = 1, 0, 0, 1
        self.ids.label_title.text = '< R E S U L T A D O >'

        self.start = False
        # Variável de contagem regressiva resetado
        total = 0
        SharedData.start = self.start
        back_button.play()
        return SharedData.start
    

    def whatToDo(self):
        """
        --> Define o que será feito em cada round.
        """
        global total

        # Variável de contagem regressiva resetado
        total = 0

        self.listOfRounds = {}
        listOfOptions = ['Beijos', 'Mordidas-Coxa', 'Mordidas-Bunda', 'Chupões', 'Chupões-X', 'Lambidas-Pescoço', 'Lambidas', 'Roçar']
        rounds = self.definitionOfRounds()
        
        for round in range(rounds):
            time = self.definitionOfTime()
            round = random.choice(listOfOptions)
            self.listOfRounds[round] = time
        print(SharedData.sexo)
        print(self.listOfRounds)

        formatted_text = "\n".join([f"{key}: {value} Seg.." for key, value in self.listOfRounds.items()])

        if SharedData.sexo == 'Feminino':
            self.ids.label_sexo.color = [1, 0.3, 0.3, 1]
            self.ids.label_sexo.text = SharedData.sexo
        else:
            self.ids.label_sexo.color = [0, 1, 1, 1]
            self.ids.label_sexo.text = SharedData.sexo
        self.ids.label_result_timing.text = formatted_text

        # Redefinição do titulo
        self.ids.label_title.text = '< R E S U L T A D O >'

        self.start = True
        SharedData.start = self.start

        tuin.play()
        return self.listOfRounds, SharedData.start
    
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
            self.ids.label_sexo.text = ''
            self.ids.label_result_timing.text = ''
            self.ids.button_comecar.background_color = 1, 0, 0, 1
            self.ids.label_title.text = 'J O G A N D O'

            global total  # Declare total como uma variável global
            total = sum(self.listOfRounds.values())

            def atualizar_contagem(dt):
                global total  # Acesse a variável global
                self.ids.label_result_timing.text = str(total)
                self.ids.label_result_timing.font_size = font_timing
                total -= 1
                if total < 0:
                    self.ids.label_result_timing.text = "Tempo esgotado"
                    total = 0
                    self.ids.label_result_timing.font_size = font_text_menu
                    finish_time.play()
                    return False

            Clock.schedule_interval(atualizar_contagem, 1)

            SharedData.start = False
            
        else:
            pass
        