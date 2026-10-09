#THE TASK
#Implement tests that test the implementation of value from the bank file 

#Thoughts...
#String starts with "hello" == return value 0
#String starts with "h" but not hello == return value 20 
#String starts with anything else == return value 100 

#Test
#Function value() receives a string and returns an int
#Function value() handles capitalization
#Function value() must not call print()
#Function main() handles input and printing 



#SOLUTION
#3 test functions -> hello, h, and everything else 

#Import the function to be tested from bank 
from bank import value 

#Define first test function / bucket
def test_hello():
    assert value("Hello, I am Maxim") == 0 
    assert value("HELLO") == 0 
    assert value("Hello, MAXIM my name") == 0 

#Define second test function / bucket
def test_h_not_hello():
    assert value("hi there") == 20
    assert value("HOWDY partner") == 20 
    assert value("Hey there") == 20  

#Define third test function / bucket
def test_other():
    assert value("Good morning") == 100
    assert value("Great day to you") == 100
    assert value("Well hello to you") == 100  

#Run this command in terminal: python3 -m pytest Lesson_6/Lesson_6_Cases/test_bank.py -v