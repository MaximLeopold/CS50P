#The task is to create a tip calculator

#Structure:
#Main function asks for meal cost as string 
#Support function #1 turns string into float 
#Main asks for tip percentage as string
#Support function #2 turns percentage into float
#Main calculates tip amount and prints it 

#We create the support function #1 that receives a string variable and converts it to integer 
#The support function needs a parameter as placeholder so it can accept an input from the main function 
def dollar_to_float(dollar): 
        #We will receive the meal amount as input from the main function and transform it into a new variable
        #We edit the string to remove the dollar sign and then transform the variable into a float (we use a function and a method)
        dollar_new = float(dollar.replace("$", ""))
        #We return the new variable back to the main function
        return(dollar_new)

#We create support function #2 that receives a string variable and converts it to integer 
#Again the support function needs a parameter as placeholder 
def percent_to_float(percent):
        #We receive the desired tip percentage as input fron the main function and transform it into a new variable
        #We edit the string to remove the % sign and then transform the variable into a float (we use a function and a method)
        percent_new = float(percent.replace("%", ""))/100 
        #We return the new variable back to the main function
        return percent_new 

#Now we write the main function
#Main function does not need paramter - no input 
def main():
        print("Hello, I will help you to calculate the tip for your meal today")
        #Now we combine two functions - we ask the user for input and send it to the support function and store that output 
        meal = input("How much did your meal cost? ")
        meal = dollar_to_float(meal)
        percentage = input("What percentage would you like to give as tip? ")
        percentage = percent_to_float(percentage)
        final_tip = meal * percentage 
        #We must use the f string function to insert another variable into a string (otherwise we would literally print "leave ${final_tip}")
        print(f"leave ${final_tip}") 

#Call main function
main() 