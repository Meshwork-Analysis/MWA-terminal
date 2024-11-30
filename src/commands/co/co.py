import json

from ...errors.errors import OptionNotFound

from ...pathScript.config import Remove
from ...pathScript.config import AddSlug
from ...pathScript.config import Getpath

def co(option):
    # print(option)

    structure = ""
    with open("config.json") as json_file:
        json_data = json.load(json_file)

        structure = json_data['structure']

    module = Getpath()[1:].split('/')[0] # Remove forward / first
    RtnString = f'''All Current Options in Module: {module}'''
    Remove(Getpath())

    # if len(Getpath()[1:].split('/')) > 1:
    #     AddSlug(module)
    #     # Delete other option

    newpath = "/"+module
    found = False
    # print("MODDD=== "+module)
    for i in structure:
        if i[0] == module:
            for x in range(len(i)-1):
                # print(i[x+1])

                # RtnString = RtnString + "\n---" + i[x+1]
                if i[x+1] == option.lower():
                    newpath = newpath + "/" + i[x+1]
                    # print(i[x+1])
                    found = True
                # i[x+1] == option

    if found == False:
        return OptionNotFound()
    AddSlug(newpath)
    return 'Succesfully changed Option [0]'

