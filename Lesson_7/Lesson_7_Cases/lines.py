#TASK
#Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines
#If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit
#Assume that any line that starts with #, optionally preceded by whitespace, is a comment


#Thoughts...
#We must build system that: given the path to a Python file, count how many lines contain code—not blank lines and not full-line # comments
#3 core elements:
#Validate one command-line argument (user invoked the program correctly)
#Open requested python file (use try and except - think FileNotFoundError)
#Examine each line and only count code lines, return answer (start count at 0, inspect line by line, count lines in relevant categories/count correct lines)

#We use sys.argv as list containing words to start the program from the terminal -> to use it import sys 
#The important detail is that sys.argv[0] is always the program’s own name - the user’s first argument begins at index [1]
#From the task instructions one command line argument means len(sys.argv) == 2 


#SOLUTION

#Import sys
import sys 

#Check the command line argument - enforce one command line means length == 2 -> use conditionals
#If the length of sys line is not ==  2 exit program 
if len(sys.argv) != 2: #len() method and the terminal command line as input
    sys.exit("Incorrect amount of argumets- 1 command line only") #sys.exit leaves program so we don't need else statement 

#Program continues here is len == 2...

#We create a variable and store users argument/input in it -> because 
filename = sys.argv[1] #The index starts at [0] so [1] is the entered file name -> take string at index 1 of sys.argv 

#Then check if filename ends with ".py" -> if not, exit
if not filename.endswith(".py"): #Conditional if but with not as Boolean operator that reverses True/False -> then method endswith() on variable filename
    #The evaluation of boolean True or False happens from the inner expression outward
    sys.exit("Not a Python file") 

#Don't know if file actually exists -> stage 2 

#Check must now attempt to open file and exit if file doesn't exit (successfully opening the file proves that it exists)
#We use try and except to control the flow -> try statement for exception handling... 
#Then we create a loop -> Count at 0, visit every line, decide whether that line counts, increase a running total when it counts, print the final total
try: 
    with open(filename, "r") as file: #using with keyword + open() to open sys.argv[1] in read mode and saving this temporary object as "file" 
        count = 0 #Create a count for the line examination logic -> could also be global variable but more logical inside with section and prior loop 
        for line in file: #create for loop to iterate over every line in the file (file object so iterations are over individual lines)
            #Different items define next iteration differently -> string = characters, list = items, file = lines etc. 
            
            #Define first condition -> if the line is blank  
            if line.strip() == "": #remove whitespaces from beginning and end via strip() (return is either T/F)
                continue #continue if True  -> Stop the current loop iteration immediately and begin the next iteration (next line and start from top)

            #Define second condition -> if the line is a comment (starts with #, optionally preceded by whitespace)
            elif line.lstrip().startswith("#"): #remove whitespaces from left side + ask if string starts with specific characters (return is either T/F)
                continue #continue if True -> Stop the current loop iteration immediately and begin the next iteration (next line and start from top)

            else: #If the loop iteration has reached this far the line is code and is added to the count variable (then loop goes again)
                count = count + 1 
    
#Exception of try code block -> if FileNoteFoundError occurs then run this block of code instead 
except FileNotFoundError: #This is exactly what happens when file is not found -> we predict FileNotFound Error! 
    sys.exit("File is not found") #sys.exit to exit the program  

print(f"The total lines of code in this document are {count}")