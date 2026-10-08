#Module to test the convert function from Lesson_6_pytest_2

import pytest #Import pytest

#Familiarize with pytest library via help(pytest) and print(pytest.__doc__)
help(pytest)

from Lesson_6_pytest_2 import convert #Import the convert function we want to test 

def test_convert():
    assert convert(1) == 149597870700 #check the conversion between au to meters
    assert convert(50) == 7479893535000 

#Test does convert function raise a TypeError if wrong variable type given as input

def test_error():
    with pytest.raises(TypeError):#Context manager -> run convert with a certain input
        convert("1") #If 1 is given as input we expect a TypeError 

def test_float_conversion(): #Now test float conversion not integer
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1) #pytest.approx() allows for wiggle room / flexibility on what is accepted
    #,abs=0.1 determines the amount of wiggle room 