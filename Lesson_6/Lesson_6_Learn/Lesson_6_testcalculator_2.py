#The purpose of this file is to test the square function in the Lesson_6_UnitTest#1 file
#It is a unit test that checks if the square function behaves correctly for specific inputs.

#Let us import the function


from Lesson_6_unittest_1 import square #We are importing the square function from the other file 

def main():
    test_square() #We are calling the test function to run the tests

def test_square(): #When testing a function we create a new function naming it test_functionname() - this is standard convention
    try:
        assert square(2) == 4 #assert is a (new) keyword that checks if the condition is true, if not it raises an AssertionError
    except AssertionError: #Execute code in this block only if the try block raises an AssertionError (the test failed)
        print("Test failed!")
    try:
        assert square(-3) == 9 
    except AssertionError:
        print("Test failed!")
    try:
        assert square(0) == 0 
    except AssertionError:
        print("Test failed!")
    else:
        print("All tests passed!") #If all tests pass print this (else)

if __name__ == "__main__": #This ensures the main() function is only executed directly when the file is run directly, not when it is imported as module in another file -> if imported then __name__ will not equal "__main__" but will equal the module name (e.g. Lesson_6_testcalculator_2) 
    main()

