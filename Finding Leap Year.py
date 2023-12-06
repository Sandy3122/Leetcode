'''
Finding Leap Year
'''


def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
print(isLeapYear(2020))
print(isLeapYear(1800))
print(isLeapYear(2023))
print(isLeapYear(1991))