#Packages 
#3rd party library -> contains modules and packages that are not part of the standard library
#PyPI -> Python Package Index -> a repository of software for the Python programming language

#pip is the package installer / manager -> run a command to download a package that didn't come with python



#API -> Application Programming Interface -> a set of functions and procedures that allow the creation of applications that access the features or data of an operating system, application, or other service
#Package "requests" -> allows you to send HTTP requests using Python (as if the program is a web browser) and access the response data

import requests 

response = requests.get("https://www.google.com") #get retrieves the HTML content of the page and returns a response object containing the server's response to the request
#sends a GET request to the specified URL and returns a response object containing the server's response to the request

print(response.text) #returns the response content as text

