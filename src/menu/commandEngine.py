import pandas as pd
import json

from src.commands.lm.lm import lm
from src.commands.help.help import helpCMD
# from config import pathSlug, Add , Remove

version = ""
with open("config.json") as json_file:
    json_data = json.load(json_file)

    version = json_data['version']



def commandEngine(command):
    command = command.upper()
    # print(command)
    with open("Commands/commands.json") as json_file:
        try:
            json_data = json.load(json_file)
            # print(json_data[command])
            match json_data[command]:
                case "HELP":
                    print(helpCMD())
                case "LM":
                    print(lm())
                    # pathSlug = pathSlug + "asdfs"
                    # print(pathSlug)
                    # Add('/fiancials/liquid')
                    # print(pathSlug)
                    # Remove('/liquid')
                    # print(pathSlug)
                    
                    
        except:
            print(f'MWA Terminal-{version}: Command not found: {command}')
    return 'Command Engine'


