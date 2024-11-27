import datetime
from src.logger.logger import logtrail
from src.menu.commandEngine import commandEngine
from config import Getpath

def input_Dialogue():
    choice = input(f'{datetime.datetime.now()}-({'gavin'})-{Getpath()}: ')
    if choice.upper() == 'EXIT':
        print('Goodbye! :)')
        return False
    if ( len(choice) != 0) and (not (choice.upper == 'EXIT')):
        commandEngine(choice)
    logtrail(f'{datetime.datetime.now()}-({'gavin'})-{Getpath()}: {choice}')
    return True


