#OBJECT ORIENTED PROGRAMMING 
#Object-oriented programming (OOP) is a way of organizing a program around objects: values that keep related data and behavior together (e.g. variables/informations and actions)
#Object-oriented programming is a style of organizing code by combining related information and behavior into objects -> we create an object that owns both its information and its behavior vs. thinking only in terms of individual variables and functions 

#A class is a blueprint defining what a kind of object stores and can do
#E.g. think of a dictionary that groups information on a student together -> but does not define what information is supposed to be contained by a student or what actions he/she can do in the program 

#Notes on classes 
#A class can also contain functions describing what its objects can do/not do (function inside a class is called method)
#Inheritance lets one class reuse and extend another class (e.g. use functions/methods)
#Property allows control over how an attribute is accessed or changed (security checkpoint protecting attribute/s)
#Class methods work with the actual class instead of one specific object in the class (cls vs. self)
#Static methods belong to the class conceptually but need neither object nor class itself (behaves like an ordinary function but is just placed inside a class e.g. for organization purpose)
#Special methods define how objects should interact with built-in operations in Python (__XY__)

#A class describes a thing -> an object is one example of such thing 
#EXAMPLE (we have skipped the set up/creation of the class and objects)
#harry = Student("Harry", "Gryffindor", 1)
#Student is the class
#harry is a variable
#The value stored in harry is an object
#harry is one instance of the Student class
#name, house, and year are attributes belonging to that object

#Why use classes:
#Without classes, related information might be spread across separate variables or loosely structured dictionaries - A class creates a clear abstraction with rules
#The rest of the program can work with a meaningful XY value rather than repeatedly managing its internal pieces
#Classes are especially useful when:
#many values share the same structure;
#data and the functions operating on it belong together;
#values must obey validation rules;
#implementation details should be hidden behind a simple interface.