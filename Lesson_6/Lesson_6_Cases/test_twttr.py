#THE TASK 
#Create one or more functions that collectively test the implementation of the shorten thoroughly

#Thoughts...
#We need to test the shorten function
#Purpose: does it return the input word with all uppercase and lowercase vowels omitted?
#Input Categories: string - but what input variables/categories may force an error?
#How should we organize/theme the checks into test functions? -> Recognize vowels & remove vowels 

#Test
#Lower/Uppercase vowels removed
#Consonants remain
#Numbers remain
#Spaces and punctuation remain
#Characters remain in original order
#String without vowels remains unchanged.
#String containing only vowels becomes an empty string.
#Empty string remains empty.

#SOLUTION 

#Import the function we want to test
from twttr import shorten 

#Define the first test function / bucket 
def test_lowercase_vowels():
    assert shorten("Twitter") == "Twttr" #Insert input into the function we are testing and set it equal to the expected output 
    assert shorten ("aeiou") == "" #All (lowercase) vowels should be removed 

#Define second test function / bucket 
def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == "" #All (uppercase) vowels should be removed 

#Define third test function / bucket
def test_consonants():
    assert shorten("rhythm") == "rhythm" 

#Define fourth test function / bucket
def test_empty():
    assert shorten("") == "" 

#Define fifth test function / bucket
def test_rest():
    assert shorten("S1mple. Test!") == "S1mpl. Tst!"

#Run this command in Terminal: python3 -m pytest Lesson_6/Lesson_6_Cases/test_twttr.py