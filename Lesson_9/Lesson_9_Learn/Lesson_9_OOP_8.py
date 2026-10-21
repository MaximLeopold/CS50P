#Object Oriented Programming 
#Operator overloading -> implement your own interpretation (e.g. + does not equal addition) when they are used with objects from your own class
#Operations include:
#+
#-
#*
#==
#<
#>

#For built in values/objects Python knows how the operators should behave 
#2 + 3          # 5
#"Hi" + "!"     # "Hi!"

#Operator overloading lets your own classes define their version of +, ==, and other operators

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0): #the other values are set to 0 meaning they are not required
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self): #Determine how the class is printed/shown (otherwise print below won't work!)
        return f"{self.galleons} , {self.sickles}, {self.knuts}"

    #Introduce special method using operator overloading
    def __add__(self, other): #Teaching Python how to "add" two Vaults together -> otherwise the operator wouldn't work! 
        galleons = self.galleons + other.galleons 
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts) #creating the new object of the vault class using Vault() to add the content of the self vault and other vault 


potter_family = Vault(100,50,25) #Creating fault for potter family with money inside 
print(potter_family) 

weasley_family = Vault(25, 50, 100)
print(weasley_family) 

total = potter_family + weasley_family
print(total) 

#Now we want to combine the content of two Vaults -> operator overloading 
#object.__add__(self, other) 

