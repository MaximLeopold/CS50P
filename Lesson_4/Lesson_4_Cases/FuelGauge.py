#THE TASK
#Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full
#Implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank 
#If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full
#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError

#Thoughts...
#User must be prompted for a fraction -> if not fraction error/return or handle that error 
#Code then transforms fraction into percentage 
#Extra conditions for 1% or 99% 


#The solution architecture is something like:



#SOLUTION

#Ask user for input and store string as variable fraction
#We use try because we want to predict a ValueError (e.g. cat/4)
#We use a loop because we need to loop until we get a valid input -> while loop because nr. of attempts unknown 
while True:
    try: 
        fraction = input("What fuel level do you have?:Fraction ")
        #Now we split the fraction into two values  
        x, y = fraction.split("/")
        #Convert strings to ingeraters for operations
        x = int(x)
        y = int(y)
        percentage = round((x/y) * 100) #New local variable for the converted output
    except (ValueError, ZeroDivisionError): #Anticipating two possible errors 
        print(f"Enter a valid fraction - {fraction} not valid")
        continue #Starts the next loop iteration and asks user again

    if x < 0 or y <= 0 or x > y: #Conditions 
        continue 

    break #Break out of the loop 

if percentage <= 1: #No longer part of the loop 
    print ("E")
elif percentage >= 99:
    print ("F")
else:
    print(f"{percentage}%")



