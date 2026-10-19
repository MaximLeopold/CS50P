#RegEx available in library/module re

#Example function from re
#re.search(pattern, string, flags=0) 

#Several patterns exist via symbols
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {x} x repetitions
# {x,y} x-y repetitions 
# ^ matches start of the string
# $ matches the end of the string 
# [] set of characters (match)
# [^] complementing the set (cannot match)
# A|B either A or B
# (...) a group
# (?:...) non-capturing version 

#Different pre-set configurations exist for symbols/patterns (capital rule see below)
# \w = word character
# \W = not word character 
# \d = decimal digit
# \D = not decimal digit
# \s = whitespace characters
# \S = not whitespace

#flags:
#re.ignorecase
#re.multiline 
#re.dotall


#Import regular expressions
import re #regex


#Ask user for email input
#Method strip() to clean up leading or trailing whitespaces 
email = input("What is your e-mail? ").strip() 

#re.search(pattern, string, flags=0) 
#Can use \ special character to input a literal . as requirement (not just any character)
#r input as beginning of string means raw string -> pass it literal e.g. the \ no new line
if re.search(r"^\w+@(\w+\.)?\w+\.edu$)", email): #
    print("valid")
else:
    print("invalid") 


   