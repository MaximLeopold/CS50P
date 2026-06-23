#Task is to implement a program that prompts the user for input and then outputs that input in lowercase

#We create a variable and use the input function to prompt and store input from the user
prompt = input("Please give me some input ")

#Now I have to transform the input that is stored in the variable (it is already in string format)
#We can use the method .lower to convert the string variable into lowercase and have it printed back to the user
#The .lower method does not need an argument inside the () because it is a method that is called on the prompt variable itself 

print(prompt.lower())
