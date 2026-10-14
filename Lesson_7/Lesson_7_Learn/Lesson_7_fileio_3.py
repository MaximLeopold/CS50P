#Continue File I/O 

#We want to read the content in the existing file 

#With operator / context manager 
with open("names.txt", "r") as file: #Open method -> as file is the variable created/saved -> "r" just read/open file 
    lines = file.readlines() #open files come with the method readlines() -> reading lines in a file , storing in the variable n (we can use variable for other)

for line in lines: #For loop because we have a set amount of lines 
    print("hello,", line.rstrip()) #We perform the method .rstrip() on the object line 

