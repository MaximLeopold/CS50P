#Write system asking for twitter profile url and extract solely the username


#Solution without Regex


url = input("What is the URL to your profile ?").strip() 

username = url.replace("https://twitter.com/", "") #Replace 
#replace() method for strings - argument 1: what to replace, argument 2: replace with 
#Alternative removeprefix() method 
print(f"username: {username}") 


#Solution with Regex functions and methods 


import re 

url = input("What is the URL to your profile ?") 

#Substitute using RegEx -> 
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) #Use \ to accept . in regex and use ? to make s option e.g. http 
    #New function re.sub() -> substitute
#re.sub(pattern, repl, string, count=0, flags=0) 
#re.sub() argument 1: pattern, argument 2: replacement, argument 3: string/where to replace, argument 4: count, argument 5: flags 


#Other solution with Regex functions and methods 


import re 

url = input("What is the URL to your profile ?").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/.(+$)", url, re.IGNORECASE) 
#re.search() searches for Regex pattern in the variable url 
#re.search() will return the matches captures from the Regex (if present)
#(+$) would be the captured username
#?: Lets you group something in Regex but the group is not stored for after -> ie lets you group something for regex work but don't have to store it even tho not used after

#If there is a match then (boolean)
if matches: 
 print(f"Username:", {matches.group(1)}) #group 1 is (+$) so the username -> remember the other group() used ?: so not stored 
 #, separates two arguments passed to print() function
 #print "Username:" and content of group 2 in variable matches 