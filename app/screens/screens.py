import os
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
    """
    --> Classe para compartilhar dados entre as telas.
    """
    start = None
    escolhaSexo = None
    difficult = None
    sexo = None
    


class DifficultyMode(Screen):
    font_column = NumericProperty(font_column)
    font_row = NumericProperty(font_row)
    font_button = NumericProperty(font_button)
    font_text = NumericProperty(font_text)
    font_text_menu = NumericProperty(font_text_menu)
    font_title = NumericProperty(font_title)
    font_start = NumericProperty(font_start)
    font_timing = NumericProperty(font_timing)
    
    def definitionOfDifficultyEasy(self):
        SharedData.difficult = 'Easy'
        click_button.play()
        pass


    def definitionOfDifficultyHard(self):
        SharedData.difficult = 'Hard'
        click_button.play()
        pass


    def definitionOfDifficultyExtreme(self):
        SharedData.difficult = 'Extreme'
        click_button.play()
        pass


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
        SharedData.escolhaSexo = self.sexo
        click_button.play()
    
    
    def definitionOfSexWomen(self):
        """
        --> Define o sexo como Feminino ao clicar no botão.
        """
        self.sexo = 'Feminino'
        SharedData.escolhaSexo = self.sexo
        click_button.play()
    

    def definitionOfSexRandom(self):
        """
        --> Define o sexo como aleatório ao clicar no botão.
        """
        listOfSex = ['Random']
        self.sexo = random.choice(listOfSex)
        SharedData.escolhaSexo = self.sexo
        click_button.play()

    def backButton(self):
        back_button.play()
        pass


class ExibirResultados(Screen):
    """
    --> Menu com os resultados das variantes.
    """
    def __init__(self, **kw):
        super().__init__(**kw)
        self.listOfRounds = {}
        self.image_path = 'app/media/images/pexels.jpg'
        
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
        if SharedData.difficult == 'Easy':
            listOfOptions = [
                'Beijos', 'Beijos', 'Massagem', 'TirarPeça', 'Drink-3', 'Drink-3', 'Arrepio', 'Cafuné'
                ]
        elif SharedData.difficult == 'Hard':
            listOfOptions = [
                'Beijos', 'Beijos-Pescoço', 'Sexo-Oral', 'Algemar', 'Parte-Do-Corpo(Drink)', 
                'Drink-5', 'Drink-5', 'FotoSexy', 'FotoSexS2', 'VideoS2'
                ]
        elif SharedData.difficult == 'Extreme':
            listOfOptions = [
                'Beijos-Pescoço', 'Oral-Em-Pé', 'Oral-Sentado(a)', 'De-Quatro', 'De-Costas', 'Tesoura-Aberta', 'Por-Cima', 'Na-Parede', 'Drink-5', 'Drink-5', 'Drink-5'
                ]

        rounds = self.definitionOfRounds()
        
        for round in range(rounds):
            time = self.definitionOfTime()
            round = random.choice(listOfOptions)
            self.listOfRounds[round] = time
        print(SharedData.escolhaSexo)
        print(self.listOfRounds)
        
        printTotal = 0
        for valor in self.listOfRounds.values():
            printTotal += valor
        formatted_text = "\n".join([f"{key} = {value} Seg.." for key, value in self.listOfRounds.items()]) + f"\n\nTotal = {printTotal} Seg.."

        if SharedData.escolhaSexo == 'Feminino':
            SharedData.sexo = 'Feminino'
            self.ids.label_sexo.color = [1, 0.3, 0.3, 1]
            self.ids.label_sexo.text = SharedData.sexo

        elif SharedData.escolhaSexo == 'Masculino':
            SharedData.sexo = 'Masculino'
            self.ids.label_sexo.color = [0, 1, 1, 1]
            self.ids.label_sexo.text = SharedData.sexo
        elif SharedData.escolhaSexo == 'Random':

            SharedData.sexo = random.choice(['Feminino', 'Masculino'])
            if SharedData.sexo == 'Feminino':
                self.ids.label_sexo.color = [1, 0.3, 0.3, 1]
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

            global total
            total = sum(self.listOfRounds.values())

            def atualizar_contagem(dt):
                global total 
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
        