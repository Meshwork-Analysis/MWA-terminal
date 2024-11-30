import json
import sys
# sys.path.append("..")
from ...pathScript.config import AddSlug, Getpath, Remove

# from src.pathScript.config import Getpath 
# from src.pathScript.config import Remove,AddSlug

def cm(ModuleName):
    # module = input('what module would you like to change to?')


    structure = ""
    with open("config.json") as json_file:
        json_data = json.load(json_file)

        structure = json_data['structure']

    Newpath = ''


    for i in structure:
        if i[0] == ModuleName.lower():
            Newpath = Newpath + i[0]
    
    if Newpath == '':
        print('Error [404] - Module Not Found')
        Newpath = Getpath().replace('/','')
        return f'Using Current Path /{Newpath}'


    oldPath = Getpath()

    Remove(oldPath)

    AddSlug("/"+Newpath)

    return f'succesfully changed modules /{Newpath}'




# oldPath = Getpath()

# Remove(oldPath)

# AddSlug('sdf')