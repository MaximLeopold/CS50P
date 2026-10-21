#New Object-Oriented-Attribute: Properties 


#A getter and setter let a class control what happens when one of its attributes is read or changed 
#The problem -> Attributes created from/in a class can be changed later to an invalid value (even if you validate the original value inside __init__)
#-> original value inside __init__ is valid but then later replaced with an invalid value/input (validation created inside __init__ only checks the value when the object is first created - not after / during modification) 
#E.g. student=Student("Harry", "Gryffindor") and later student.house=Amsterdam
#The solution = making the object a property with a getter (for reading) and setter (for changing)

#A getter is a method that controls what happens when an attribute is read -> e.g. print(student.house)
#The @property decorator makes the method behave like an attribute

#A setter is a method that controls what happens when someone assigns a new value to an attribute
#Assigning is -> student.house="Ravenclaw" 
#The setter is called/used to check if the assignment is valid or invalid before storing it 
#@XY.setter 

#Setter and getter functions need _ before the name of the object/property (same name but add _)

#The setter function is called either during initializing or during modification afterwards -> hence all verification can be placed inside the setter and can be removed from __init__ (because __init__ also calls the setter)



class Student: 
    def __init__(self, name, house, patronus):
        if name == "": 
            raise ValueError("Wrong Input for Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Wrong Input for House") 
        else: 
            self.name = name #instance variable (can't also have a function with that name - will collide)
            self.house = house #instance variable (^...)
            self.patronus = patronus #instance variable (^...)

    def __str__(self): 
        return f"{self.name} from the house {self.house} with the patronus {self.patronus}"


    #Getter
    @property
    def name(self): #Getter only takes one argument 
        return self._name #must use _ 

    #Setter 
    @name.setter #Getter & setter naming same -> property created above must match the naming 
    def name(self, name): #Setter takes at least 2 arguments
        if name == "": #Other notion for if not name
            raise ValueError("Not good") #use raise to envoke Errors by our choosing
        else:
            self._name = name 


   #Getter -> function for/in a class that gets an attribute
    @property #use to define / set-up a getter and name function exactly like the property 
    def house(self):
        return self._house #MUST use _ based on the setter below 
    
    #Setter -> function for/in a class that sets an attribute (attach a setter to the property created above)
    #Use this code/method when someone assigns a value to the property house 
    @house.setter #use to define the setter (house refers to the property created above)
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Not good")
        else:
            self._house = house #MUST use _ to create almost identical name to the object? 
    
    def charm(self): 
        match self.patronus: 
            case "Stag":
                return "𓅃"
            case "Snake":
                return "𓆗"
            case _: 
                return "na"

def main():
    student = get_student()
    print(student)
    print(student.charm()) 

def get_student():
    name = input("name") 
    house = input("house") 
    patronus = input("patronus") 
    return Student(name, house, patronus) 
   
if __name__ == "__main__":
    main() 