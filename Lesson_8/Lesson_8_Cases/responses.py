#The task
#Using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address
#You may not use re. And do not validate whether the email address’s domain name actually exists


#Thoughts...
#User input is the email 
#Check e-mail / verification
#True or False / print (boolean)


#SOLUTION


#Import relevant library/module
from validator_collection import checkers 
#Validator collection -> multiple modules and tools 
#Module checkers -> groups functions that answer yes/no questions by returning True or False
#E.g is_email(), is_integer(), is_url(), is_file() etc. (T/F)


#Ask user input email 
email = input("What is your e-mail address ")


#Start email verification 
#Use the module checkers and the relevant function is_email() (from library validator_collection)
#One function inside the checkers module - checks whether a supplied value resembles a syntactically valid email address

#email variable passed into is_email() -> returns true or false 
check = checkers.is_email(email) 

if check is True: #Is the same as just "if check" -> because is_email() already retrusn either True or False 
    print("Valid e-mail")
else:
    print("Invalid e-mail") 
