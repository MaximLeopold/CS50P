#Libraries in Python

#Reusable code is called a library -> collection of functions, methods, classes etc. that allow you to perform many actions without writing your code
#Python has a rich set of libraries and modules that can be used for various purposes (e.g. numphy)
#Modules are files containing python code -> can define functions, classes, variables etc. -> can be imported and used in other python programs
#1) Standard library built into python -> no need to install (pre installed)
#2) Third party libraries -> need to install using pip (package manager for python) -> pip install library_name

#Some functions are built into python but must be imported from a module in the standard library
#E.g. math module contains mathematical functions and constants -> import math -> math.sqrt(16) returns 4.0

import random #Import the random module from the standard library -> contains functions for generating random numbers and performing random operations
coin = random.choice(["heads", "tails"]) #choice is the function stored in the module random -> Randomly selects and returns one of the items from the list
#output stored in variable coin and "" formating used to create list of strings
print(coin)

#from -> keyword to use for important functions from a module instead of importing entire module 
from random import choice #Import only the choice function from the random module 
#Now we can use just choice() instead of random.choice() during coding 

#New function from shuffle module -> shuffle does not return a new list but shuffles the original list in place
cards = ["jack", "queen", "king", "ace"]

random.shuffle(cards) 
print(cards)

#IMPORTANT
#If you have a larger project with several folders and python files functions and variables do not automatically become available to other files in the project #You need to import them using the import statement:

#Two import styles:

#1)Import entire module
#import module_name (this is just the file name) -> use module_name.function_name() to access functions in the new/current module (file name)

#2)Import specific functions from a module
#from module_name import function_name -> use function_name() to access the function in the new/current module (file name)  

#IMPORTANT: If the files are in different folders you need to use dot notation to specify the path to the module/file you want to import 
#E.g. -> from folder_name.module_name import function_name -> use function_name() to access the function in the new/current module (file name) 
#module_name is the name of the file