#Conditionals
#Used to control the flow and execution of code 


#if condition - runs if condition is met
#elif condition - runs if previous condition was not met and it is met 
#else - runs is nothing above was met 

#Logical Operators
#and - both conditions must be met
#or - one condition must be met
#not - reverse condition 
#match match the variable/condition via cases 

#Comparison Operators
# == equal to
# != not equal to
#< > >= <= basic math 
#% means remainder (e.g. 3 / 5 has a remainder of 2)

x = int(input("What is x? "))
y = int(input("What is y? "))

#We use conditions
if x < y:
    print("x is less than y ")
elif x > y:
    print("y is less than x ")
elif x == y:
    print("x and y are equal ")
else:
    print("You are confusing me ")

#We can combine conditions
if x < y or x > y:
    print("x is not equal to y ")
else:
    print("x is equal to y ")

