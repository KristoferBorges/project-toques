import random
from time import sleep

def definitionOfRounds():
    rounds = random.randint(1, 3)
    return rounds


def definitionOfTime():
    time = random.randint(10, 40)
    return time


def definitionOfSex():
    listOfSex = ['Masculino', 'Feminino']
    sexo = random.choice(listOfSex)
    return sexo


def whatToDo():
    listOfRounds = {}
    listOfOptions = ['Beijos', 'Mordidas-Coxa', 'Mordidas-Bunda', 'Chupões', 'Chupões-X', 'Lambidas-Pescoço', 'Lambidas', 'Roçar']
    rounds = definitionOfRounds()
    
    for round in range(rounds):
        time = definitionOfTime()
        round = random.choice(listOfOptions)
        listOfRounds[round] = time
    print(listOfRounds)
    return listOfRounds

#whatToDo()
#definitionOfSex()
#definitionOfRounds()
#definitionOfTime()
