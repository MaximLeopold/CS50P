#Introduction to Object-Oriented Programming -> Class 
#Class as variable type -> create and design your own data types 
#We can standardize/control what attributes can be and what values can be set/assigned 
#Classes come with methods/functions we can use to determine behavior 

#Keyword for exceptions -> raise (create your own exceptions)

#Special functions in Classes (functions in classes are called methods)...

#1   __init__ -> how a new object of/in the class should be initialized
#Calling the class creates the object, and __init__ puts its initial information into it
#def __init__(self, XY1, XY2, ...) the attributes 
#self.XY1 = XY1 ... 
#Create an object of/in the class -> variable XY = ClassName(Input for XY1, XY2, ...) (Python then calls __init__)
#Access attributes later e.g. print(XY.XY1)

#2.  __str__ -> how this object should be shown as text/string 
#Python calls __str__ automatically when it needs a readable string representation of a object
#def __str__(self): (only receives argument self -> because other arguments/parameters are stored in self and can be accessed)
    #returnf"{self.attribute} {self.attribute}"
#



#Keyword class
#Capture all intended functionality inside the class 
#We are adding variables to objects 
class Student: #This is my own "data type" (class)
    def __init__(self, name, house, patronus): #Initialize contents of an object of a class - function to customize class's objects
       #Create validation in the class -> ensure objects created are valid (all functionality inside the class)
        if name == "": #If name is empty then
            raise ValueError("Wrong Input for Name")#Raise a value error and print message message for error raised
        #Raise another if condition
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: #If input for house not in this list then... 
            raise ValueError("Wrong Input for House") 
        else: 
            self.name = name 
            self.house = house
            self.patronus = patronus 

    #Define a second/custom function in the class
    def __str__(self): #Only one argument -> self so you always have access to function
        return f"{self.name} from the house {self.house} with the patronus {self.patronus}"
    #Here we use self.XY because the values belong to a particular student/class object 
    #Python needs to know whose name, house, etc. -> self refers to one specific student and the data stored
    #Self gives the method access to the particular object currently using the method, including that object’s stored attributes

    #Define a second/custom function in the class
    def charm(self): #Must always have minimum self as argument
        match self.patronus: #match means examine value and find matching case (similar to if and elif e.g. if self.patronus == stag return XY)
            case "Stag":
                return "𓅃"
            case "Snake":
                return "𓆗"
            case _: #Every other possible value -> _ is the match content equivilant of else 
                return "na"


def main():
    student = get_student()
    print(student)
    print(student.charm()) #Calling two different functions print() and charm() 


def get_student():
    name = input("name") #Attribute 1 (instance variables) 
    house = input("house") #Attribute 2 (instance variables)
    patronus = input("patronus") #Attribute 3 (instance variables) 
    return Student(name, house, patronus) #Treat class as function -> constructs a class (student) object using class as template (every object is structured the same/from the class template)
    #Student() is the function of class -> standardizing how to pass data/info into the student class
    #Calls the __init__ function / pre work done
   

if __name__ == "__main__":
    main() 