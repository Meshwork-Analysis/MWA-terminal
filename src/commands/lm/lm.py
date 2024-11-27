import json
def lm():
    structure = ""
    with open("config.json") as json_file:
        json_data = json.load(json_file)

        structure = json_data['structure']

    RtnString = f'''------All Current Modules------'''


    for i in structure:
        RtnString = RtnString + "\n" + i[0]



    return RtnString