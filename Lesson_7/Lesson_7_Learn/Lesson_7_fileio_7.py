#short lesson on reading and writinf files 

#See what is inside the file -> then extract text from file 

def main():
    with open("book.md", "r") as f: #with statement as context manager + function open() to open a file -> second argument how to open
        contents = f.readlines() #use readlines() method on the variable f and store in variable contents 
    
    chapter1 = contents[3:9] #We now want to use readlines() only on lines 3 to 9
    with open("chapter1.txt", "w") as f: #We want to create a new file saving chapter1
        f.writelines("chapter I.") #use the write() method on object f to write in the file

main()

#Ensure Terminal location matches directory containing the files (Lesson 7)
#Enter cd Lesson_7/Lesson_7_Learn -> move terminal
#Enter python3 Lesson_7_fileio_7.py
