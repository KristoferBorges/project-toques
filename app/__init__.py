import os
from pygame import mixer

# Definição de caminhos absolutos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_click_button = os.path.join(diretorio_atual, 'media', 'sounds', 'click_button.mp3')
caminho_tuin = os.path.join(diretorio_atual, 'media', 'sounds', 'Tuin_Editado.MP3')
caminho_startGame = os.path.join(diretorio_atual, 'media', 'sounds', 'Start_Editado01.MP3')
caminho_back_button = os.path.join(diretorio_atual, 'media', 'sounds', 'back_button.MP3')
caminho_finish_time = os.path.join(diretorio_atual, 'media', 'sounds', 'finish_time.MP3')
caminho_backgroound_image = os.path.join(diretorio_atual, 'media', 'images', 'pexels.jpg')

# Sounds
mixer.init()
click_button = mixer.Sound(caminho_click_button)
tuin = mixer.Sound(caminho_tuin)
startGame = mixer.Sound(caminho_startGame)
back_button = mixer.Sound(caminho_back_button)
finish_time = mixer.Sound(caminho_finish_time)

# Images
background_image = caminho_backgroound_image