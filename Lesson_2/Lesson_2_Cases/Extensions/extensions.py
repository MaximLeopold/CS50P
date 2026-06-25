#The goal is to implement a program that prompts the user for the name of a file and then outputs only the file's media type if the file's name ends, case-insensitively, in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip 
#If the file name ends with some other suffix or has no suffix at all the output should be "application/octet-stream"


#We ask for input and remove the capitalization up front 
#We can use the .endswith() operation here 
answer = input("what is the file name you want to upload? Please give the full name and file type ").lower()

#We build our logic 
if answer.endswith(".jpg") or answer.endswith (".jpeg"):
    print("image/png")
elif answer.endswith(".gift"):
    print("image/gift")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream") 


