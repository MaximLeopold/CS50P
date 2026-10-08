#Pytest is 3rd party program -> automating testing of code 
#Library that allows us to write tests for our code and run them automatically 
#Instead of manually calling each test function you write test functions using normal Python and let pytest find them, execute them, and report failures -> your test functions must begin or end with "test" so pytest can find them e.g. test_square() or square_test() 

#There are other testing libraries but pytest is popular and widely used (entry point)

#Install pytest by inserted this prompt in Terminal (install)
#Enter this command: python3 -m pip install pytest

#We now use pytest to test the square function in the Lesson_6_unittest_1.py file 

from Lesson_6_unittest_1 import square #We are importing the square function from the other file

import pytest #Importing the pytest library 

#When testing use assert 
#The logic is to break tests into themes/buckets (e.g. positive numbers vs. neg.) for easier error handling and deduction/fixing 

def test_positive(): #When testing a function we create a new function naming it test_functionname() - this is standard convention
    assert square(2) == 4 #Now we use the function we are testing and assert the exepcted output from a defined input 
    assert square (3) == 9 
    assert square (2) == 4  

def test_negative():
    assert square (-3) == 9
    assert square (-2) == 4

def test_zero(): 
    assert square (0) == 0

#Now we are testing for string values as input -> we check if the function square() produces the correct error if a string is given as input
#We are testing if the function raises a TypeError when the input value is a string 
#pytest.raises -> tells pytest which error you expect 
def test_str():
    with pytest.raises(TypeError): #We use the "with" statement/context-manager construct -> perform this code under a particular context 
        square("cat") #We must use "" to create a string value 

#Enter this command in the Terminal: python3 -m pytest Lesson_6/Lesson_6_Learn/Lesson_6_pytest.py