#Unit Tests
#Writing code that tests your code - catching errors and ensuring code works as intended
#Unit test is a small piece of code that automatically checks whether one specific part—or “unit”—of your program behaves correctly

#A unit test is a function that tests another function (focused on specific aspects of the code) 
#Give a function an input, then check whether its behavior matches what you expect
#We can use the normal operators e.g. == , !=, > etc. 
#We can use Boolean True or False e.g. assert is_adult(18) is True


def main():
    x = int(input("What is x? "))
    print("x squared is", square(x)) 

def square(n):
    return n * n

if __name__ == "__main__": #This ensures the main() function is only called when the file is run directly, not when it is imported as module 
    main()  

#When we import a file we want to access/use the functions in it but we don't want the code to just run automatically 

#The if name = main aspect allows the code to be run as a script or imported as a module without running the main function automatically! 
#The if __name__ == "__main__": main() line is a common Python idiom that allows a file to be both run as a script and imported as a module without executing the main function automatically

#Python changes the value of __name__ depending on how the file was opened (imported or directly), and the if statement uses that value to decide whether to call main() -> if file started directly then call main(), if file imported then don't call main() automatically 

#When you run the file directly, __name__ equals "__main__", so main() runs
#When another file imports it, __name__ equals the module’s name, so main() does not run automatically
