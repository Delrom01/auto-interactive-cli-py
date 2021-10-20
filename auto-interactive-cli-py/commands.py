from colorama import *

init()


class Instances:

    def __init__(self)-> None:
        print(Fore.YELLOW + """--- Initialisation des instances nécessaires ---""" + Fore.RESET)
        self.var_1 = 2
        self.var_2 = False


    def __del__(self)-> None:
        print(Fore.YELLOW + """--- Suppressions des instances ---""" + Fore.RESET)


    def read_file(self, file_name: str, file_yes: int) -> None:
        """

        Args:
            file_name (str): Nom du fichier à lire
            file_yes (int): Un entier

        Returns:
            nothing
        """
        print(f"Test de lecture dans le fichier : {file_name}")
        print(file_yes)


    def write_file(self):
        print("Test d'ecriture dans un fichier")


    def modif_instance_var_1(self):
        self.var_1 = self.var_1 + 1
        print(Fore.YELLOW + "commande exécutée" + Fore.RESET)


    def print_instance_var_1(self):
        print(self.var_1)


    def exit(self):
        pass
