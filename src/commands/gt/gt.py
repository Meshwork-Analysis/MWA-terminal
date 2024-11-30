from ...errors.errors import OptionNotFound, ModuleNotFound
from ...pathScript.config import Getpath, Remove, AddSlug
import json

def gt(inputpath):

    # Currentmodule = ''
    # print('were in with' + str(inputpath.lower()))
    # if not Getpath() == '':
        
    #     Currentmodule = Getpath()[1:].split('/')[0] # Remove forward / first
    # # Currentmodule = Getpath() # Remove forward / first

    # print('wtf???'+ Currentmodule)

    # CurrentOption = Getpath()[1:].split('/')[1] # Remove forward / first



    Remove(Getpath())
    # inputpath = str(inputpath.lower)


    if not len(inputpath.lower()[1:].split('/')) ==2:
        return "Please input both the module and option"
    newModule = inputpath.lower()[1:].split('/')[0]

    # print('sdfas' + newModule)
    newOption = inputpath.lower()[1:].split('/')[1]

    newpath = "/"


    structure = ""
    with open("config.json") as json_file:
        json_data = json.load(json_file)

        structure = json_data['structure']



    foundOP = False
    foundMD = False
    for i in structure:
        # print('afsa '+i[0]+" asdfdasf" + newModule)
        # for x in i:
            # print(x)
        if i[0] == newModule:

            # print('found--- '+ i[0])
            newpath = newpath + newModule
        #     print(newpath)
            foundMD = True
            for x in range(len(i)):
            # for x in i[0]:
                # print(i[x] , " sdfa")
                if i[x] == newOption:
                    newpath = newpath + "/" + str(i[x])
                    foundOP = True
                    # print('FOIUNDDD')
        elif foundMD == False:
            return ModuleNotFound()
    if foundOP == False:
        return OptionNotFound()
    
    # print(newModule)
    AddSlug(newpath)

    return 'Successfully changed Path'
 
