import json

from ...errors.errors import BadUse

from ...pathScript.config import Getpath
def lo(module):
    structure = ""
    with open("config.json") as json_file:
        json_data = json.load(json_file)

        structure = json_data['structure']
    if module == '':
        module = Getpath()[1:].split('/')[0] # Remove forward / first
        
    RtnString = f'''All Current Options in Module: {module}'''
    

    if module.lower() == '':
        return BadUse()
    for i in structure:
        if i[0] == module.lower():
            for x in range(len(i)-1):
                RtnString = RtnString + "\n---" + i[x+1]


    return RtnString