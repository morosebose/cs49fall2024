"""
leap_year.py

Check whether a given year is a leap year. 

Programmer: Surajit A. Bose, Date: 2024.11.01
"""

def main() :
    # Get input from user
    year = int(input("Enter a year: "))
    
    # if the year is not divisible by 4, it is not a leap year
    if (year % 4) != 0 : 
        is_leap = False
    # if the year is divisible by 4 but is a century year, e.g. 1900, 
    # further check if it is divisible by 400 
    elif (year % 100  == 0) and (year % 400 != 0) :
        is_leap = False
    # The year has passed all tests for leapiness
    else :
        is_leap = True
    
    # print results
    if is_leap :
        print(f'{year} is a leap year.')
    else :
        print(f'{year} is not a leap year.')
        
if __name__ == "__main__" :
    main()