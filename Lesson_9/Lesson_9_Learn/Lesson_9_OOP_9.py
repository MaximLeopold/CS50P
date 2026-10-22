#Object Oriented Programming - Shorts content/lessons



#Short on Classes...



class Package:
    def __innit__(self, number, sender, recipient, weight): #The self refers to the object we can create from the class
        self.number = number 
        self.sender = sender 
        self.recipient = recipient
        self.weight = weight
#Why the self.XY = XY?
#To store the supplied weight permanently inside the newly created object -> Take the temporary value supplied as the weight parameter and save it in this particular object under the attribute name weight 
#self.weight = attribute stored in object - weight = parameter temporary input
#Self refers to the object -> every object / instance gets its own stored weight value 
#The parameters (right side) could technically have different names 

#When creating a new object/instance not all parameters must be stored (stored only if needed later for that object)
#E.g. -> storing a new object of the Class Square
#Entering the width and height but only storing the area 
#def __init__(self,width,height):
#   self.area = width * height 

#Creating an object/instance of the Package class 
package_1 = Package(1, "Maxim", "Peter", 5) #Information is assigned in order of attributes in innit 



#Short on Class Methods and Class Variables...



class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients) #Classname.classmethod

#Creating a class variable -> shared across all objects/instances of a class 
    base_hearts = 1 

#Creating a class method -> functionality beloning to the class
#To do so we have to decorate via @classmethod
    @classmethod 
    def calculate_hearts(cls, ingredients): #The function always takes ingredients as input/parameter (cls always first input)
        hearts = cls.base_hearts #accessing the class variable (same as Food.Base_hearts -> bec. Python passes the class name into cls or in other words use the base_hearts belonging to whichever class called this method
        #Cls is only available inside a class method that declares it as a parameter (outside the method it has no meaning)
        for x in ingredients: #For loop saying for every ingridient add +1 
            if "hearty" in x.lower(): #conditional 
                hearts = hearts + 2 
            else: 
                hearts = hearts + 1 
        return hearts #return calculated amount of hearts 

#Creating a class method
#cls creates new instance of the class -> override default values for hearts from class variable -> return special instance 
    @classmethod
    def from_nothing(cls, hearts): #instead of supply ingridients -> supply hearts the food should give despite ingridients 
        food = cls(ingredients=[]) 
        food.hearts = hearts
        return food  

def main():
    stew = Food(["mushroom", "hearty meat", "water"]) #Parameter can receive any Python value, inc. a list containing several values
    print(f"This meal {stew} gives {stew.hearts} hearts")

    pie = Food.from_nothing(hearts = 3) #using class method in combination with creating new instance of class food 

main() 



#Short on instance variables


#self refers to new instance of the class created through init function
#Inputs after self are inputs that are then assigned to the instance of the class
#self.number etc. are instance variables
#When creating instance below (Package(1, "Maxim" ...)) we assign input to the instance variables that then gets assigned to the self / specific instance of the class 
class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number 
        self.sender = sender 
        self.recipient = recipient
        self.weight = weight

def main():
    packages = [ #Create list
        #Inside list create new instance of the class Package -> calls init function from the class (new instance supplied as "self")
        #Arguments are matched to the paramters via positioning (1-4)
        #In the init function 1, "maxim", "Tim", 10 are temporarily assigned to the right side 
        #The left side is the actual attribute being created/saved with that information in the new object/instance  
        Package(1, "Maxim", "Tim", 10), 
        Package(2, "Maxim", "Puck", 5)  #Create second instance -> remember need the , after list items! 
    ]

    for x in packages: #For loop -> for every package in the list "packages"
        print(f"{x.number} sent from {x.sender} to {x.recipient}") #Accessing information stored in instances of the class 
            
#E.g. this is also valid
#class Package:
    #def __init__(self, x, y, z, w):
        #self.number = x
        #self.sender = y
        #self.recipient = z
        #self.weight = w
#self.number etc. remain the attributes that are stored and accessed later (x,y,z,w are not!) 
#Can also change the left side e.g. self.package_number = x 
#However, can't change right side and not top! e.g. self.number = package_number but top is self, x, y, z, w)



#Short on instance methods



class Package:
    def __innit__(self, number, sender, recipient, weight): #The self refers to the object we can create from the class
        self.number = number #Collection of instance variables that are created every time a new instance of the class is created via innit function 
        self.sender = sender 
        self.recipient = recipient
        self.weight = weight

#Encapsulating functionality in the class
#Instance methods -> method (a kind of function) is part of a class 
    def __str__(self):
        return f"{self.number} sent from {self.sender} to {self.recipient}"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [ #Create list
        Package(1, "Maxim", "Tim", 10), 
        Package(2, "Maxim", "Puck", 5)  #Create second instance -> remember need the , after list items! 
    ]

    for x in packages: 
        print(f"{x} and costs {x.calculate_cost(cost_per_kg=2)}") 