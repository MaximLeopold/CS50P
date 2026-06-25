#The task is to implement a program that prompts the user for a greeting. If the greeting starts with "hello" output $0. If the greeting starts an "h" but not "hello" output $20. Otherwise output $100. 

#We can not use the in statement because it matches exactly - any other included words would distort the output 
#We can use the .strip and .lower methods/operations to support the program (remember methods are like functions that belong to a string variable)
#We have to use the () at the end to call the methods/operations 

greeting = input("Hello, please introduce yourself and greet me ").strip().lower()

if greeting.startswith("hello"):
    print("$100")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$0")

