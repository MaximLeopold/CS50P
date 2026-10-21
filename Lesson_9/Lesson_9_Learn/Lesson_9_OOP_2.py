#Object Oriented Programming Technique 

#Variables -> Tuple, List, Dictionary 
#Tuple variable type -> collection of values (similar to a list but can't be changed / values can't be altered)
#Create via () e.g. return (x, y) = tuple vs. return [x, y] = list 
#Why use a tuple > list -> programming defensively or knowing that the values should not be changed 
#Numeric indexing used for tuples and lists vs. key/string indexing used for dictionaries 

def main():
    student = get_student()
    if student["name"] == "Padma": #If the key name in dictionary student is assigned the value Padma then...
        student["house"] = "Ravenclaw" #Change the value assigned to the key house in that dictionary 
    print(f"{student['name']} from {student['house']}") #Accessing information stored in the list using indexing 
    #Must use single quotes inside the double quotes otherwise SyntaxError 

def get_student():
    name = input("name")
    house = input("house")
    return {"name": name, "house": house} #create and return dictionary all at once  

if __name__ == "__main__":
    main() 