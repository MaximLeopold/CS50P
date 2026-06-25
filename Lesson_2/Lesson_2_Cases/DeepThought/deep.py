#The goal is to implement a program that prompts the user for the answer to a question and outputs yes if the user inputs 42, forty-two, or forty two  (case insensitively) and otherwise says no

answer = input("Do you know the answer to the golden question? ")

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print ("Yes - correct")
else:
    print ("No - not the answer I am looking for") 

#Alternatively we can use if and in 
#In means is this value one of the options? 
#We use {} to make a dictionary but () would also work 

if answer in {"42", "forty-two", "forty two"}:
    print ("Yes - correct")
else:
    print ("No - not the answer I am looking for")