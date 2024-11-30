import pandas as pd
import json

from src.errors.errors import CommandNotFound, InDev, ParameterAbuse
from src.commands.co.co import co
from src.commands.lo.lo import lo
from src.commands.cm.cm import cm
from src.commands.lm.lm import lm
from src.commands.gt.gt import gt
from src.commands.help.help import helpCMD
# from config import pathSlug, Add , Remove

version = ""
with open("config.json") as json_file:
    json_data = json.load(json_file)

    version = json_data['version']



def commandEngine(command):
    commandFirst = command.split(' ', 1)[0].upper()
    # print(command)
    with open("src/commands/commands.json") as json_file:
        try:
            json_data = json.load(json_file)
            # print(json_data[command])
            match json_data[commandFirst]:
                case "HELP":
                    print(helpCMD())
                case "LM":
                    print(lm())
                case "CM":
                    if len(command.split(' ', 1)) == 2:
                        print(cm(command.split(' ', 1)[1].upper()))
                    else:
                        print(ParameterAbuse('cm','moduleName'))
                        # print("Incorrect number of params - 1 required - enter: 'cm ModuleName' - please see 'help' to insert correct command")
                case "LO":
                    # print(lo())
                    if len(command.split(' ', 1)) == 2:
                        print(lo(command.split(' ', 1)[1].upper()))
                    else:
                        # print(ParameterAbuse('lo','ModuleName'))
                        print(lo(''))
                        # print("Incorrect number of params - 1 required - enter: 'lo ModuleName' - please see 'help' to insert correct command")
                case "CO":
                    if len(command.split(' ', 1)) == 2:
                        print(co(command.split(' ', 1)[1].upper()))
                    else:
                        print(ParameterAbuse('co', "optionName"))
                        # print("Incorrect number of params - 1 required - enter: 'co OptionName' - please see 'help' to insert correct command")
                case "GT":
                    if len(command.split(' ', 1)) == 2:
                        print('going in??')
                        print('PAPRAM: '+command.split(' ', 1)[1].upper())
                        print(gt(str(command.split(' ', 1)[1].upper())))
                    else:
                        print(ParameterAbuse('GT','ModuleName/OptionName'))
                    # pathSlug = pathSlug + "asdfs"
                    # print(pathSlug)
                    # Add('/fiancials/liquid')
                    # print(pathSlug)
                    # Remove('/liquid')
                    # print(pathSlug)
                case "RUN":
                    print(InDev())
                    
        except Exception as err:
            # print(f'MWA Terminal-{version}: Command not found: {command}')
            print(CommandNotFound(command))
            # print(err)
    return 'Command Engine'


