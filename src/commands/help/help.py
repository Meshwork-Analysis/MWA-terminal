import json


version = ""
authors = ""
with open("config.json") as json_file:
    json_data = json.load(json_file)

    version = json_data['version']
    authors = json_data['authors']


helpdialogue = f'''----HELP MENU----
\nVersion: {version}
\nAuthors: {authors}
\n----Commands----
\n(Note: Commands aren't case sensitive, they work both upper and Lower Case)
\ncm = Change Module (works from anywhere)
\nco = Change Option (works from inside the module)
\ngt = Go to (Go to /module/option)
\nlm = list modules (works from anywhere)
\nlo = list options (works from inside the module)

\n----Manual----
\nWhat are Modules?: Modules are large sections of the software with individual options within them, for example: The Financials module has several options such as Profits, Losses, Liquidity and ETC
\nWhat are Options?: These are smaller tools within modules
'''

def helpCMD():
    return helpdialogue
