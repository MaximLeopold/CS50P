#Create program that asks for name and home and adds that information as new row into csv file 

#Import csv module from Python -> tools for reading and writing with csv files 
import csv 

#Ask for user input and store in variables -> currently saved in program memory but not permanently 
name = input("What is your name? ")
home = input("Where is your home? ")

#Open a file with append mode -> using "w" mode would erase existing content prior to writing 
#If students.csv does not exist, append mode will create it new 
#Open() python build in function -> receives two arguments: file to open and "a" open in append mode
with open("students.csv", "a") as file: #Open() returns a file object -> The as file section assigns that object to the variable file
    #Otherwise file = open("students.csv", "a") -> however the with runs the code while the file is open and closes it automatically (no manual close needed)
    writer = csv.writer(file) #writer() function from csv -> creates an object that knows how to write CSV data into that assigned file
    #The function writer() is passed the content of file and executed -> then result returned by the function is passed to variable writer 
    #Exact same logic as name = input("What is your name? ") -> variable = function(arguments)
    writer.writerow([name, home]) #writerow() is a method belonging to the CSV writer object -> 

#Conceptually 
#file -> connection to students.csv
#writer -> CSV formatter that writes correctly through that connection
