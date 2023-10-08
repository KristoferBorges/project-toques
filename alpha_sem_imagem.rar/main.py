from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.support.setup import Setup
import random
import time

class Tela(App):
    """
    Classe principal do aplicativo v1.0-alpha.
    """
    def build(self):
        self.title = 'Toques'
        Setup()
        adm = ScreenManager()
        return adm


if __name__ == '__main__':
    Tela().run()