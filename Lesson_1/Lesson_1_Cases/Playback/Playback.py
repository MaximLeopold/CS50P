#The task is to create a program that prompts the user for input and then outputs that input but replaces each space with "..."

#We create a variable and use the input function to prompt the user for input and store it in that variable
prompt = input("Hello, please give me some input ")

#Now we have to transform the input that is stored in the string variable and use the print function to print it back to the user with the changes
#We can use the method .replace 
#We now need to put an argument in the method () to explain what we want - " old string " , " new string "
print(prompt.replace(" ", "..."))

