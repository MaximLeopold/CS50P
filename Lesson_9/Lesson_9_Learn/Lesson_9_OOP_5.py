#Object Oriented Programming 
 
#type() function -> lets you see the type/class of whatever the input is 
#print(type(50)) (Type/class would be int)

#Class methods -> keyword @classmethod 
#Method/function that works with the class itself rather than one particular object created from the class
#Not associate functions with ojbects of a class but rather the class itself ^
#Called/envoked using Class.example() 

#Instance method → receives self → works with one particular object (works with one object's stored data)
#Class method    → receives cls  → works with the class itself

#Import module/library 
import random 


#Create a class
#Using the class as a container -> functionality and variables limited to one instance/version of "the sorting hat" 
class Hat:
    houses = ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]

    @classmethod 
    def sort(cls, name): #cls als first argument/input for classmethod instead of self 
        house = random.choice(self.houses)
        print(name, "is in", random.choice(cls.houses)) #Variable accessible via class method 

#Create variable and create hat class object
Hat.sort("Harry") 
