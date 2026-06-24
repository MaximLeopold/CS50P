#Deciding Houses in Harry Potter

#Version 1 
name = input("What is your name ?")

if name == "Harry":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == ("Draco"):
    print("Slytherin")
else:
    print("Who are you?")

#Combine
if name =="Harry" or name == "Ron":
    print("Gryffindor")
else:
    print("Who are you?") 

#What is we had loads of differnt names?
#Use the match option - this must use "case"
#To use else in the case option we use case _: to catch everything else
name = input("What is your name?")

match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")

    case _:
        print("Who?")

#We can combine cases using | (press control + option + 7)
name = input("What is your name?")

match name:
    case "Harry" | "hermione" | "ron":
        print("Gryffindor")
    case _:
        print("wWho are you?") 