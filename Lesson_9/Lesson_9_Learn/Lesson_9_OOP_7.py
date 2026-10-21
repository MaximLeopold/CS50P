#Object Oriented Programming 
#Inheritance 
#Design classes in a hierarchy
#One class inherit or borrow attributes (methods/functions or variables) from other classes

#Super Class 
class Wizard:
    def __init__(self, name): #Attributes here then passed on initializing objects of child classes 
        if name == "":
            raise ValueError 
        else: 
            self.name = name
    

class Student(Wizard): #Class Student inherits from Wizard -> is the child class of Wizard 
    def __init__(self, name, house):
        super().__init__(name) #Using super() to access the __init__() method of the parent class and inserting name 
        self.house = house 
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) #Using super() to access the __init__() method of the parent class and inserting name
        self.subject = subject 
    ...

#create variable and assign return value of the __init__ / constructors of the respective classes
student = Student("Harry", "Gryffindor") #create a student using the Student() class and entering arguments 
professor = Professor("Severus", "Spell Defense") #...^
wizard = Wizard("Maxim") #...^