from colorama import *

init()    #for colorama


class Instances:        ######!! This file contains all the commands that can be used/launched with the cli !!######

    def __init__(self)-> None:      #function allowing to set and initialize the instances ("global variables") useful in the following functions
        print(Fore.YELLOW + """--- Initialization of the necessary instances ---""" + Fore.RESET)
        #declaration of the instances on the model :
        #self.var_1 = value_1     (value_1 is int, float, bool ...)
        #self.var_2 = value_2     (value_2 is int, float, bool ...)


    def __del__(self)-> None:       #function to cleanly delete instances
        print(Fore.YELLOW + """--- Deletion of instances ---""" + Fore.RESET)


    def function_1(self, param_1, param_2) -> None:      #function with 2 parameters in entry
        """

        Args:
            param_1: Description of the parameter param_1
            param_2: Description of the parameter param_2

        Returns:
            #if return something
        """        
        ###
        #code of the function_1
        #you can use the parameters in the following way (for exemple) :
        #print(param_1)
        ###
 

    def function_2(self):       #function with any parameters in entry
        ###
        #code of the function_2
        #you can use the instances in the following way (for exemple) :
        #self.var_1 = self.var_1 + 1
        #print(self.var_1)
        ###


    def function_3(self):       #function with any parameters in entry
        ###
        #code of the function_3
        #you can display a message in the following way (for example):
        #print(Fore.YELLOW + "message" + Fore.RESET)
    
    
    ###
    #The same goes for all the functions to be declared
    ###


    def exit(self):     #function to leave the cli
        pass
