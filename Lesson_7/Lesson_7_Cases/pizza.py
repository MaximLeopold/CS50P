#Task
#Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate
#Format the table using the library’s grid format
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit


#Thoughts...
#Check for one command line argument so length == [1] (0->1) 
#Check for one command line argument is name of a CSV file in Pinocchio's format 
#Read file content csv -> pass content onto tabulate 
#Validate command line argument, open csv file, read csv rows, format and print as table 


#SOLUTION

#Import sys
import sys 
#Import csv 
import csv 
#Import tabulate
import tabulate 

#Check the command line argument - enforce one command line means length == 2 -> use conditionals
#If the length of sys line is not ==  2 exit program 
if len(sys.argv) != 2: #len() method and the terminal command line as input
    sys.exit("Incorrect amount of argumets- 1 command line only") #sys.exit leaves program so we don't need else statement 

#Program continues here is len == 2...

#We create a variable and store users argument/input in it -> e.g. regular.csv (string telling python where file is located - does not contain actual content)
filename = sys.argv[1] #The index starts at [0] so [1] is the entered file name -> take string at index 1 of sys.argv 

#Then check if filename ends with ".csv" -> if not, exit
if not filename.endswith(".csv"): #Conditional if but with not as Boolean operator that reverses True/False -> then method endswith() on variable filename
    #The evaluation of boolean True or False happens from the inner expression outward
    sys.exit("Not a csv file") 

#Open and inspect the csv file (should be either regular.csv or sicilian.csv)
try:
    with open(filename, "r") as file: #filename contains path as string -> file is the opened readable connection to the object/file (IT IS A CONNECTION NOT THE ENTIRE FILE/CONTENT)
        #Now need to understand the file 
        reader = csv.reader(file) #reader() csv reader produces parsed rows -> adds interpretation layer to understand file contents (in this case csv specific/Python's module for csv) 

        #Now format reader content with tabulate() from module tabulate
        formatted_table = tabulate.tabulate(reader, headers="firstrow", tablefmt="grid")
        #First argument table's data source -> use rows produced by reader as table data 
        #Second argument headers -> keyword argument to use firstrow values as headings -> can also do headers="keys" for dictionaries
        #Third argument table format-> controls presentation / can be controlled with many styles

        print(formatted_table)
        #All of this stays in the with block
        #Because the reader still depends on the open file 

except FileNotFoundError:
    sys.exit("File not found ") 

