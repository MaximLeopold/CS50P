#Object Oriented Programming
#Creating functionality specifically within a class via @classmethod 
#Design principle to include relevant functionality in the class (prefered over random functions outside the class))

class Student: 
    def __init__(self, name, house):
            self.name = name #instance variable (can't also have a function with that name - will collide)
            self.house = house #instance variable (^...)

    def __str__(self): 
        return f"{self.name} from the house {self.house}"

#Include functions / class functionality inside the class itself
#Create class method
    @classmethod 
    def get_student(cls): #new function set inside the class (classmethod = can call this method without initializing a student object or having one created already)  
         name = input("name")
         house = input("house")
         return cls(name, house) #creating a new object -> use cls() instead of get() 

def main():
    student = Student.get_student() #We are using the classmethod get() from class Student -> the get/create new student functionality is built into the class itself! 
    print(student)

#Conditional to avoid accidentally invoking main when creating module or package 
if __name__ == "__main__":
    main() 