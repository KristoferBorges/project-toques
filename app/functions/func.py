import random
from time import sleep

def definitionOfRounds():
    rounds = random.randint(1, 3)
    return rounds


def definitionOfTime():
    time = random.randint(10, 40)
    return time


def whatToDo():
    listOfRounds = {}
    listOfOptions = ['Beijos', 'Mordidas', 'Chupões', 'Lambidas', 'Roçar']
    rounds = definitionOfRounds()
    
    for round in range(rounds):
        time = definitionOfTime()
        round = random.choice(listOfOptions)
        listOfRounds[round] = time
    print(listOfRounds)
    return listOfRounds

whatToDo()
