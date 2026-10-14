#Library for working with csv files (comma seperated values)
#Module csv 

import csv #import the csv library -> contains tools designed specifically for CSV files

#Functions include:
#csv.reader() , csv.writer(), csv.DictReader(), csv.DictWriter() -> we need the . infront the function to access the library 

#create empty list -> will eventually contain all student dictionaries (one per student)
students = []

with open("students.csv") as file: #open() function opens a file and returns a file object then assigned to the variable file 
    #The returned object file from open() represents a connection between the program and the students.csv file 
    #We use with bec. it keeps the file open while running the block of code -> when execution leaves the block the file automatically closes
    #Otherwise/without with -> we need to close the file with file.close() 

    reader = csv.reader(file) #The function reader() is from the csv library - we are reading file -> we can also use csv.DictReader()
    #reader() function creates the reader object returned by the function which is then assigned to the variable reader (not the function itself but the object)
    for name, home in reader: #Iterrating over the reader and not the file itself via for loop -> sequence unpacking 
        students.append({"name": name, "home": home}) #create a dictionary and append to the list students

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student["name"]} is from {student["home"]}") 


#CSV reader advantage -> don't have to rely on getting a row as list and using [][] and unpack them manually 
#We can store the names of columns in the csv file itself (e.g. simply name,home)