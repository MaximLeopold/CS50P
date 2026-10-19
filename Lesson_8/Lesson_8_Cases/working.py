#The task
#Implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 09:00 to 17:00)
#Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each
#Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically
#Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.) - but do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM)


#Thoughts...
#Input string
#    ↓
#1. Validate and extract both times
#    ↓
#2. Convert each time from 12-hour to 24-hour
#   ↓
#3. Assemble and return the final string

#Convert function
#Start hour, start minute, start period, end hour, end minute, end period 


#THE SOLUTION


#Import Regex module/library 
import re 

#Define main function 
def main():
    hours = input("What are your hours? ")
    print(f"Your hours are: {convert(hours)}") #Pass value stored in hours into support function convert() and return to print


#Define support function #1
def convert(x):
    #Must determine whether the entire input follows one exact structure (start hour, minute, period + end hour,minute,period)
    #Use re.fullmatch() -> returns match object/true if entire string fits the pattern provided 

    #Define the pattern as seperate variable for simplicity of code
    pattern = r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)"
    #6 patterns in regex
    #(start_hour), (start_minute), (start_period), (end_hour), (end_minute), (end_period) 

    match = re.fullmatch(pattern, x) #The Regex pattern saved in variable pattern above inserted as argument for the regex pattern -> attached/stored in local variable match 
    #re.fullmatch() returns a match object when successfully but none when unsuccessful 

    #Therefore handle the exception 
    if match is None: #If the entire pattern did not match with the user input in hours passed into convert(x) 
        raise ValueError #Expected errortype 

    #If the match variable is not None then continue...

    #Retrieve the group values from match variable and assigning them to six local variables inside convert() function
    #Use groups() method on match variable to return a tuple of the 6 pattern groups captured -> ie give me the contents of all your captured groups (start hour, start minute....end minute, end period)
    captured_values = match.groups()
    #Then assign groups to local variables specifically using indexing
    start_hour = int(captured_values[0])
    start_minute = captured_values[1] #Problem case (see below)
    start_period = captured_values[2]
    end_hour = int(captured_values[3])
    end_minute = captured_values[4] #Problem case (see below)
    end_period = captured_values[5]

    #Handle complications -> an omitted minute right now is none but it is actually 00 
    if start_minute is None:
        start_minute = int(0)
    else:
        start_minute = int(start_minute)

    if end_minute is None:
        end_minute = int(0)
    else:
        end_minute = int(end_minute)

    #Use support function #2 to convert the time correctly - based on captured 6 groups 
    start_time = convert_time(start_hour, start_minute, start_period)
    end_time = convert_time(end_hour, end_minute, end_period)

    #Return to main()
    return (f"{start_time} to {end_time}") 


#Define support function #2
def convert_time(hour, minute, period): #Define 3 paramters -> local placeholders for variables inputted into function 
    if period == "AM" and hour == 12: #if condition handles midnight -> e.g. 12:00 AM turned to 00:00 
        hour = 0 #Single == assigns vs. double == compares / T or F result
    elif period == "PM" and hour != 12: #if condition handles evening -> e.g. 1 pm turned to 13 
        hour = hour + 12 #Single == assigns vs. double == compares / T or F result
    return f"{hour:02}:{minute:02}" #return both variables using at least 2 digits 



if __name__ == "__main__":
    main() 