# from src.menu.input_Dialogue import input_Dialogue
from src.menu.input_Dialogue import input_Dialogue
import os


os.system('cls' if os.name == 'nt' else 'clear')

print(''' __   __ _     _ _______   _______ _______ ______   __   __ ___ __    _ _______ ___     
|  |_|  | | _ | |   _   | |       |       |    _ | |  |_|  |   |  |  | |   _   |   |    
|       | || || |  |_|  | |_     _|    ___|   | || |       |   |   |_| |  |_|  |   |    
|       |       |       |   |   | |   |___|   |_||_|       |   |       |       |   |    
|       |       |       |   |   | |    ___|    __  |       |   |  _    |       |   |___ 
| ||_|| |   _   |   _   |   |   | |   |___|   |  | | ||_|| |   | | |   |   _   |       |
|_|   |_|__| |__|__| |__|   |___| |_______|___|  |_|_|   |_|___|_|  |__|__| |__|_______|''')

print('Type "Help" to see a list of all the commands, \nEnjoy Using MWA Terminal :)')



lp = True
while lp:
    lp = input_Dialogue()