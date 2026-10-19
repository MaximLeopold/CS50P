
#Import library for Regex
import re 



name = input("What is your name ?").strip()
matches = re.search(r"(^.+), (.+)$", name) #re.research() function from re library 
#re.search() returns a match object if pattern is founded -> assigned to variable matches (if the suggested pattern isn't found the result is none) 
#Looks for the pattern "Lastname, firstname" in previous input 
#() inside the re.search() create capture group -> capture those characters as group

if matches is not None: #if the result of re.search() stored in matches is true / if matches is not none (if the pattern was found) 
    last = matches.groups(1) #last name from regex group 
    first = matches.groups(2) #first name from regex group 
    #grousp() method does match object -> returns portions captured by parentheses in the regex - Returns a tuple of the 2 groups in the regex
    name = f"{first} {last}" #reassign the content to variable name / change content from original stored input 

#If the user inputs the right format the complete if block is skipped... 
print(f"hello {name}") 

#New operation :=
#Assign a value and ask a boolean question about it on the same line / same time (e.g. if statement)
#E.g. if matches := re.search (r"(^.+), (.+)$", name):
#   name = matches.group(2) + " " + matches.group(1) 