#Create a grading systems

score = int(input("What was the score? "))
if score >= 90 and score <= 100:
    print("Congrats. Grade A ")
elif score >= 80 and score < 90:
    print("Nice. Grade B ")
elif score >= 70 and score < 80:
    print("Decent. Grade C")
else:
    print("mhmmm... you passed ")

#Improve the code - increase efficiency, reduce risk of bugs, and increase readability 
#Nest questions together and remove the and condition
if 90 <= score <= 100:
    print("Nice. Grade A ") 

#Determine if x is even or odd
x = int(input("What is x? "))

if x % 2 == 0:
    print("Even ")
else:
    print("Odd")

#Create a function that determines if a number is even or odd
#We can include a function even if it doesn't exist yet ("is_even")
def main():
    x = int(input("What is x ?"))
    if is_even(x):
        print("Even ")
    else: 
        print("Odd ")

def is_even(n):
    if n % 2 == 0:
        #We can return a bool value / variable (they can only be True or False)
        #Bool is a new variable type
        #Use return to send the True or False back into the main function for it to make the decision
        return True 
    else:
        return False

#We can combine if and else into one line
#Same example from above but combined and improved 
def is_even(n):
    return True if n % 2 == 0 else False 

#Improved again
def is_even(n):
    return n % 2 == 0