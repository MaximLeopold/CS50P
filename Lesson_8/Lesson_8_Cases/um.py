#The task
#implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word
#E.g given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0
#Additionally implement, in a file called test_um.py, three or more functions that collectively test your implementation of count thoroughly, each of whose names should begin with test_


#Thoughts...
#count() must accept string, find every um, ignore capitalization, count um only as complete word/not part of other words, and return an integer 
#Goal: how do we distinguish string um standalone from part of other word e.g. yummy? -> Regex word boundary \b
#Need .IGNORECASE to accept Um UM um etc. 
#Need raw string r"..." to accept Regex backslashes 
#Support function to find all matches 
#len() to turn matches into final count 

#input string
#    ↓
#find all standalone, case-insensitive occurrences of "um"
#    ↓
#collection of matches
#    ↓
#length of that collection
#    ↓
#integer returned by count()


#SOLUTION


#Import relevant module -> Python’s built-in Regex module
import re
#Re contains relevant functions e.g. re.search(), re.match(), re.findall(), re.sub() etc. 

#Define main function 
def main(): #ask user → call count() → print result
    text = input("Give me the text ") #Ask user for input of the text to be analysed and store in variable text 
    print(f"The um count is: {count(text)}") #Pass the content of variable text into the function count() and print the result returned (will be an int.)
     

#Define support function 
def count(x): #receive string → calculate count → return integer
    #main() passes variable text into the function count() -> value stored in variable text is passed into function and assigned to local parameter x
    #Paramter is a local name that receives data from its caller 

    #re.findall(pattern, string, flags) -> searches entire string and returns all non-overlapping matches in a list
    #Assign the result to a variable 
    findings = re.findall(r"\bum\b", x,re.IGNORECASE) #Use r raw string to preserve backslashes for the regex - without r Python interpret \b as a backspace character instead of regex rule 
    #Pattern/Regex -> \b is word boundary therefore we find all patterns that have: boundary, um, boundary in local variable x 
    #re.ignorecase makes it case insensitive

    return len(findings) #Find the length of output of findall() to return number of matches (result was stored as list e.g. findings = ["Um", "um", "UM"]) 
    #len() function already creates an INT so no conversion needed
    #Use return keyword to end function call and pass value back to code that called the function 
    

#Make code importable / modular coding for transfering code 
if __name__ == "__main__":
    main()
