#Now let us implement that we save this information -> storing information persistently 

name = input("What is your name" )

#Function "open" -> purpose to open a file to read information or write information to it (understand as double click on something)
name_file = open("names.txt", "a") #Open() built in python function to create/open a file - Pass second argument into the function a (we want to write/append)  
name_file.write(f"{name}") #write() is the method to write whatever is stored in the variable name onto the name_file (names.txt)
name_file.close() #close() is the method to close the file 

#Remember functions() vs. methods(): Methods belong to—or operate on—a particular object (e.g. write and close)

#With is a context manager 
#with open("names.txt", "a") as file: #With -> then function / method -> then as variable_name XY (removes need to close manually)