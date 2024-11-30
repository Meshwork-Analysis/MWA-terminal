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
\ncm moduleName = Change Module (works from anywhere)
\nco OptionName = Change Option (works from inside the module)
\ngt /module/option = Go to (Go to /module/option), Remember to always include the "/" in front, and leave no trailing "/"
\nlm = list modules (works from anywhere)
\nlo Option(optional) = list options (works from anywhere), if executed with no params, then it throws a "Bad execution" error, if used within module then it lists all options of that module, if used with module entered then lists options of module

\n----Manual----
\nWhat are Modules?: Modules are large sections of the software with individual options within them, for example: The Financials module has several options such as Profits, Losses, Liquidity and ETC
\nWhat are Options?: These are smaller tools within modules, to execute the tools, use the "run" command.
'''

def helpCMD():
    return helpdialogue
