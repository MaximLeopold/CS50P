#Short lesson on writing and editing csv files 
#The views.csv file is the support file for this module

#Remember managing modules/libraries
#pip install XY   → buy and place a toolbox in your workshop (run in the terminal)
#import XY        → bring that toolbox to your workbench for this program


#Import csv module/library -> then access via dot notation e.g. csv.reader()
import csv 

#Import numpy module/library -> can also assign local name via import numpy as XY  
import numpy 

#Can also import parts of modules/libraries -> from XY import XY
#E.g. from PIL import Image -> then use function/method Image()


def main():
    with open("views.csv", "r") as file: 
        reader = csv.DictReader(file) #Use the DictReader operation and pass the file from views as input
        #Assign the result to reader so you can refer to and use the newly created DictReader object after - if we dont assign then the reader object would not save / can't do anything with it
        #Same thing as writing input("What is your name? ") without assigning anything = 
        
        #DictReader creates the rows as dictionaries -> first row as keys 
        #E.g. in a loop each iteration so each row is one dictionary
        #The normal reader() would create lists []
        for x in reader:
            print(x) #Printing the content  

if __name__ == "__main__":
    main() 
