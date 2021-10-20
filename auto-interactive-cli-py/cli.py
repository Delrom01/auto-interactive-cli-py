import questionary
import inspect
import commands    #fichier de commandes
from colorama import *

init()


def cli():
    #print("""--- Récupération des commandes (fonction) d'un module python ---""")
    commands_list = []
    search_commands = inspect.getmembers(commands.Instances, inspect.isfunction)  # commands = fichier de commandes
    #print(search_commands)
    for i in range(len(search_commands)):
        commands_list.append(search_commands[i][0])
    #print(commands_list)


    choice = questionary.select("Quelle commande voulez-vous exécuter ?", choices=commands_list).ask()


    if choice == "exit":
        exit = questionary.confirm("Souhaitez-vous annuler 'exit' ?").ask()
        print("")
        return choice, exit

    else:
        #print("""--- Récupération des arguments associés à une commande (fonction) ---""")
        args = []
        params = inspect.getfullargspec(getattr(commands.Instances, choice))
        #print(params)
        for arg in params.args:
            if arg == "self":
                pass
            else:
                args.append(arg)
        #print(args)


        if not args:
            #print("args ne contient pas d'arguments")
            #print("""--- Appel de la commande ---""")
            print("")
            getattr(Instance, choice)()
            print("")
        else:
            #print("""--- Récupération de la doc associée à une commande (fonction) ---""")
            doc = inspect.getdoc(getattr(commands.Instances, choice))
            print("")
            print("usage : commands.py [OPTION] COMMAND [ARGS]...")
            print("")
            print(doc)
            print("")
            args_values = [""]
            #saisie = ""
            for i in range(len(args)):
                saisie = questionary.text(f"Saisir une valeur pour l'argument {args[i]} : ").ask()
                #saisie = input(f"Saisir une valeur pour l'argument {args[i]} : ")
                args_values.append(saisie)
            #print("Arguments saisies :")
            #print(args_values)
            #print("""--- Appel de la commande ---""")
            print("")
            getattr(commands.Instances, choice)(*args_values)
            print("")


        exit = questionary.confirm("Voulez-vous saisir une nouvelle commande ?").ask()
        print("")
        return choice, exit


if __name__ == "__main__":
    print(Fore.YELLOW + """--- DEBUT DU PROGRAMME ---""" + Fore.RESET)
    Instance = commands.Instances()
    print("")
    saisie = cli()
    while saisie[1] == True:
        saisie = cli()
    del Instance
    print(Fore.YELLOW + """--- FIN DU PROGRAMME ---""" + Fore.RESET)

























########################################################################################################################

'''

def source_code():
    print("""--- Récupération du code source d'un module python ---""")
    source_code = inspect.getsource(commands)  # commands = fichier de commandes
    print(source_code)
    return source_code

def commands_list():
    print("""--- Récupération des commandes (fonction) d'un module python ---""")
    commands_list = {}
    search_commands = inspect.getmembers(commands, inspect.isfunction)      #commands = fichier de commandes
    print(search_commands)
    for command in search_commands:
        for i in range(len(search_commands)):
            #print(command[0])
            commands_list[i] = command[0]
    return commands_list

def command_args():
    print("""--- Récupération des arguments associés à une commande (fonction) ---""")
    # params = inspect.signature(commands.read_file)
    params = inspect.getfullargspec(commands.read_file)
    print(params)
    for args in params.args:
        print(args)

def command_doc():
    print("""--- Récupération de la doc associée à une commande (fonction) ---""")
    doc = inspect.getdoc(commands.read_file)
    print(doc)
    return doc

'''



########################################################################################################################

'''
if __name__ == "__main__" :
    functions_list = getmembers(commands)      #fichier de commandes
    #print(functions_list)
    for i in range(len(functions_list)):
        function_name = (functions_list[i][0])
        #print(function_name)
        regex = "((^[a-zA-Z0-9]+)([_]?[a-zA-Z0-9]+)+)"
        #regex = "(^[a-zA-Z0-9]+)"
        result = re.search(regex, function_name)
        if result != None:
            function_name = result[0]
            print(function_name)
'''



########################################################################################################################

'''
def initialisation():
    print("Initialisation des instances nécessaires")


def list_commands():
    commands = []
    commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../commands"))
    #print(commands_folder)
    for filename in os.listdir(commands_folder):
        if filename.endswith(".py") and filename.startswith("cmd_"):
            commands.append(filename.replace("cmd_", "").replace(".py", ""))

    commands.sort()
    return commands


def cli():
    commands = list_commands()
    choice = questionary.select("Quelle commande voulez-vous exécuter ?", choices=commands).ask()
    #folder_cmd = os.chdir('c:/Users/T0258229/PycharmProjects/questionary/commands')
    #print(choice)
    #cmd = "python ../commands/cmd_" + choice + ".py"
    #print(cmd)
    #execution = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    #stdout = execution.communicate()
    #print(stdout[0])
    exit = questionary.confirm("Voulez-vous saisir une nouvelle commande ?").ask()
    return choice, exit
    

if __name__ == "__main__" :

    print("DEBUT DU PROGRAMME")
    initialisation()
    saisie = cli()
    while saisie[1] == True:
        saisie = cli()
    print("FIN DU PROGRAMME")
'''
