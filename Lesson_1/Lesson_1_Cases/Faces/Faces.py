#The task is to create a function called convert that accepts a string as input and returns that same input with any :) converted to a smiley face emoji and any   :( converted to a sad face emoji (all other text must remain unchanged)

#In the same file create a function called main that prompts the user for input, calls convert on that input, and prints the results 

#Structure:
#User types text
#Function "main" gets the text
#Function "main" calls function "convert" with that text as argument
#Function "convert" returns the transformed text (we use the method replace and must implement the return statement)
#Function "main" prints that transformed text

#We write the convert function - we define our own function
#The function needs to take a parameter as input - this is a placeholder for whatever value gets passed into the function (we can call it anything we want)
def convert(text):
    #We use the .replace method to replace :) / :( with the corresponding emoji
    text = text.replace(":)", "😊")
    text = text.replace(":(", "😢")
    #Then we want to return the transformed text into the function main
    return text 

#We write the main function
def main():
    #We create a variable and use the input function to prompt the user for input and store it in that variable
    prompt = input("Hello, how are you feeling today? ")
    #Now we have two options:
    #A) We can create a new variable that stores the output of the convert(prompt) function and then print that new variable 
    #B) We can directly use the print function to directly print the output of the convert function that takes the variable "prompt"
    #We can not simply just call convert(prompt) because we have to do somethiing with that output - store in new variable and print or print directly
    print(convert(prompt)) 

#Now we call the main function to run the program
#The main function does not need any parameters because it is not taking any input from another function
main()