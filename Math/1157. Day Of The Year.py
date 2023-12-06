'''
1157. Day Of The Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.
'''

# Brute Force Case

# def DayOfYear(date):
#             # To Find Leap Year
#     def isLeapYear(year):
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#             return True
#         else:
#             return False
        
#     date = date.split("-")
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     daysCount = 0
#     for i in range(0, len(days)):
#         if int(date[1]) == i + 1:
#             daysCount = int(days[i + 1]) + int(date[2])

#     # Adjust for leap year if February and after February
#     if int(date[1]) > 2 and isLeapYear(int(date[0])):
#         daysCount += 1
#         return daysCount
#     return daysCount
   
# date = "2020-02-10"
# print(DayOfYear(date))




def DayOfYear(date):
    def isLeapYear(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
        
    date = date.split("-")
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysCount = int(date[2])  # Initialize with the day of the given date
    
    # Iterate through months before the given month
    for i in range(0, int(date[1]) - 1):
        daysCount += days[i]                # Add days in each month before the given month
    
    # Adjust for leap year if February and after February
    if int(date[1]) > 2 and isLeapYear(int(date[0])):
        daysCount += 1
    
    return daysCount

date1 = "2019-01-09"
date2 = "2020-02-10"
print(DayOfYear(date1))  # Output: 9
print(DayOfYear(date2))  # Output: 41












# Different Case
# def dayOfYear(date: str) -> int:
#     d = {
#         1: 0, 2: 31, 3: 60, 4: 91, 5: 121, 6: 152,
#         7: 182, 8: 213, 9: 244, 10: 274, 11: 305, 12: 335
#     }

#     year, month, day = map(int, date.split('-'))

#     sub = 1
#     if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#         sub = 0
    
#     res = day + d[month] - (sub if month > 2 else 0)
#     return res

# # Test cases
# date1 = "2019-01-09"
# date2 = "2019-02-10"
# print(dayOfYear(date1))  # Output: 9
# print(dayOfYear(date2))  # Output: 41
