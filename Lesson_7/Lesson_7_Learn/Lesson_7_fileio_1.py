#File I/O in Python
#File input/output -> letting program save information to files and retrieve it later 
#Input = reading data from a file 
#Output = writing data to a file 


#Files provide persistent storage (otherwise variables dissapear when the program ends)


#Common file modes
#r - read existing file
#w - write and replace existing content
#a - append new content to the end
#x - create new file 


#Write a program that asks for user names and saves them 

#Create an empty list - [] indicate list vs. {} dictionary  
names = []

for n in range(3): #Create for loop (placeholder variable n) -> the for loop runs 3 times -> each time receiving 0 then 1 then 2 
    name = input("What is your name? ") #Ask for name as string and store in local variable - for this itteration of the for loop 
    names.append(name) #Take string stored in local variable name / in this itteration of the for loop and add it to the end of the list "names"

for name in sorted(names): #We create a for loop to print the names stored in the list "names"
    #We use for loop because we know how many names we stored 
    #We pass the list "names" into the function sorted() to sort the str values alphabetically 
    print(f"hello, {name}")

#Now let us implement that we save this information -> storing information persistently 

with open("names.txt") as file: 
    for line in file:
        names.append(line.rstrip()) 

for name in sorted(names):
    print(f"hello, {name}")

