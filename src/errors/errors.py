import json

version = ""
with open("config.json") as json_file:
    json_data = json.load(json_file)

    version = json_data['version']


def ModuleNotFound():
    return f'MWA {version}::::Error [4343] Module Not Found'

def OptionNotFound():
    return f'MWA {version}::::Error [4344] Option Not Found'

def CommandNotFound(command):
    return f'MWA {version}::::Error [8934] Command Not Found: {command}'

def BadUse():
    return Bad Execution:::: Incorrect usage of command, refer to "help"'


def InDev():
    return 'Sorry, this feature is still in development'


def ParameterAbuse(command, typeP):
    return f'MWA {version}:::: Incorrect number of params - 1 required - enter: "{command} {typeP}" - please see "help" to insert correct command'