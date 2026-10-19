#Lecture on regular expressions
#Regex -> patterns for finding, validating, and transforming text
#Patterns  commonly written as raw strings so Python doesn’t interpret backslashes before the regex engine sees them

#Rregex functionality lives in the re module - common functions:
#re.search(pattern, text)       find a match anywhere
#re.match(pattern, text)        match from the beginning
#re.fullmatch(pattern, text)    require the entire text to match
#re.findall(pattern, text)      return all matches
#re.sub(pattern, replacement, text)  replace matches

#Regex lets you describe text pattern once and then apply to large amounts of text data automatically - common use cases:
#Validating input: emails, phone numbers, dates, usernames, postal codes
#Extracting information: finding URLs, prices, IDs, or timestamps in text
#Searching code and files: finding every function call or similarly shaped line
#Cleaning data: removing extra spaces or standardizing inconsistent formatting
#Transforming text: reformatting dates or replacing matching phrases
#Analyzing logs: locating errors, IP addresses, and request identifiers
#Web development: checking form input and parsing structured parts of URLs
#Cybersecurity and system administration: searching commands, logs, and configuration files


#Example of validation without RegEx 
#Validate e-mail address input

#Ask user for email input
email = input("What is your e-mail? ").strip() #Method strip() to clean up leading or trailing whitespaces 

#First validation attempt 
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")


#NEW VERSION


#Ask user for email input
email = input("What is your e-mail? ").strip() #Method strip() to clean up leading or trailing whitespaces 

#Second validation attempt

#User input split into two variables -> split at the @ sign into username and domain 
username, domain = email.split("@") #Asign to variables simultaneously + Method split() will split a string into multiple based on input value (remember execution right to left)

if username and domain.endswith(".edu"): #Two seperate boolean expressions if username and if .endswith()  
     print("Valid")
else:
    print("Invalid") 
