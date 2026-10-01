#THE TASK
#Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program)
#Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item #No need to pluralize the items. Treat the user’s input case-insensitively

#Thoughts...
#Repeatedly ask for an item and store in a dictionary with the item as the key and number of items it was inputted as value/on the list 
#Count the number of times each item was inputted
#Sort the list alphabetically
#Create a while loop -> unknown amounts of items -> once exit condition is met we execute operations on the list
#Important -> #if handles values and conditions you can examine - #try/except handles operations that raise exceptions.

#SOLUTION

#Create an empty dictionary to store the grocery list
grocery_list = {}

while True: #A While loop to repeatedly ask for an item (runs indefinitely -> until exit condition is met)
    #Every while loop requires a condition in order to run the loop -> True (boolean value) is just our way of saying run this loop indefinitely until we break out of it (exit condition) -> #We don't know how many items the user will input
    try: #Try means while the loop is true (currently indefinitely try performing this block of code) -> then we also have except block to handle the exit condition 
        item = input("What item are you adding to the list? ").upper() #Item user inputs during each iteration of while loop is stored in the local variabl
        if item in grocery_list: #We add conditionals -> if the item is already in the dictionary we increase the count by 1 
            grocery_list[item] = grocery_list[item] + 1 #[item] is local variable and gets the user input each time the loop iterates -> Square brackets after a dictionary variable (see {} up top) access a key inside that dictionary / perform an action on that key 
        else: #If the item is not in the dictionary  
            grocery_list[item] = 1 #We add the item to the dictionary with count 1 
    except EOFError: #If this error occurs python executes the code below and not up top -> but it is still in the while loop -> we are still in the loop
        print() #New line printed in the console for user to see 
        break #This is the actual exit condition/operation to end the while loop -> if we don't have this break statement the loop would continue indefinitely 

#Next we code what happens after the loop / exit condition has been met 
#Sort items alphabetically and print the grocery list with counts 

#Pyton has -> methods and functions 
#Methods are associated with a particular object (like a dictionary) -> we can call methods on objects using dot notation e.g. .upper 
#Functions receive the object as an argument -> we can call functions on objects using parentheses e.g. print(object/variable) or len(object/variable)

for item in sorted(grocery_list): #For loop -> iterates through grocery_list dictionary for each item -> item is the local variable (placeholder) represents each item in the dictionary every time the loop iterates -> Give grocery_list to the sorted function -> sorted function returns a new list of the items 
    print(f"You have: {grocery_list[item]}, {item}")
    #f string to combine text and variables -> anything inside {} is evaluated and inserted into the printed string 
    #Grocery_list[item] retrieves the value associated with the key (so the count of that item) -> [] for dictionary lookup 
    #The second {item} inserts the key itself (the item name) 
    