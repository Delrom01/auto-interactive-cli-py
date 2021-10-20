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
