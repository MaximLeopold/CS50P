#This is a test file for the lines.py task
#All this code is only for counting purposes 


students = []

#We want to open and read the rows in the csv file 

with open("students.csv") as file: #We do not have to specialize "r" because it is default with open -> we stored the content in variable file 
    for variable in file: #variable as placeholder variable for the for loop - file is the opened students.csv stored as variable name file above ^
        #So for every line in the variable file we will now...
        #We assign two variables at once -> sequence unpacking/multiple assignment -> we read right to left so we split the variable and then multi assign
        name, house = variable.rstrip().split(",") #rstrip() method removes whitespaces - split(",") splits the string based on the input character ","
        #Essentially you perform:
        # x = variable.rstrip().split(",")
        # name = x[0]
        # house = x[1]
        
        #We create a dictionary {} -> a dictionary with two keys name and house 
        student = {"name": name, "house": house}
        students.append(student) #We add it to the list we originally created -> remember in for loop so for every row in students.csv we append to the list 

#Define a function to get one student dictionary and return the value associated with name 
def get_name(student):
     return student["name"] #Function doesn't print the name -> return so it can be sorted()

for student in sorted(students, key=get_name): #We pass a function as argument into another function (get_name into sorted) -> no () after get_name! 
        print(f"{student["name"]} is in {student["house"]}") 
#Key= is a parameter inside the sorted() function -> you can also say e.g. sorted(students, reverse=True)
#key=get_name means here is the function you should call to determine the sorting value for every item - it uses the return value of get_name to perform the alphabetical sortation 