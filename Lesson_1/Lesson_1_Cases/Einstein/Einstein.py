#The task is to create a program that prompts the user for mass as an integer (in Kg) and then outputs the equivalent number of joules as an integer. Assume that the user will input an integer ( E = m*c^2 )

#Structure:
#Prompt the user for mass as an integer 
#Store the input as a variabl and convert it to an integer variable (int)
#Calculate E (energy) using the formula E = m*C^2 where C is the speed of light (3*10^8 m/s)
#Print the result as an integer 

#We do not have to create two functions for this problem but it is good practice

#We create a function called mass_to_energy that takes input variable and transforms it into energy using the formula
#Remember we need to include a parameter in the function so it can accept input from the main function - we also have to use the return statement to give it back to the main function
#We will build the main function to already have transformed the string input into an integer variable - the support function will only do the calculation
def mass_to_energy(mass):
    #We will receive mass as the input and then transform it into a new variable using the formula
    energy = mass * 300000000 ** 2
    #We now return the new variable energy back to the main function
    return energy 

#Now we create the main function that will prompt the user for input and pass that input to the support function mass_to_energy and then print the result
#Remember the main function does not need any parameters because it is not taking any input from another function 
def main():
    #We use the input function to ask the user for mass and store it in a variable that we pass onto the mass_to_energy function
    print("Hello, this program will help you to convert mass into energy ")
    #Remember we ask use the input function and have to convert it into an integer variable (we are using two functions)
    mass = int(input("How much mass would you like to convert? "))
    #Now we have two options: create new variable that stores the output of mass_to_energy(mass) and then print that new variable or directly use print function to print output of the mass_to_energy(mass) function 
    print(mass_to_energy(mass)) 

#Now we call the function
main()