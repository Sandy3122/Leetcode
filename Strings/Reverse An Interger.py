'''

Reverse An Integer

input n = 12345678
output = 87654321

'''



'''
Brute Force Case
'''

# def reverseInt(n):
    # str_n = str(n)

    # rev = str_n[::-1]
    
    # int_n = int(rev)
    # return int_n



'''
We will convert the number to a string using StringBuffer after this, we will reverse that string using the reverse() method 

corner case 

Input: 32100

So for the above input if we try to solve this by reversing the string, then the output will be 00123.

So to deal with this situation we again need to convert the string to integer so that our output will be 123
'''

# def reverseInt(n):
#     # Converting number to string
#     str_n = str(n)

#     # Reversing the string
#     str_n = list(str_n)
#     rev = str_n.reverse()
#     rev = "".join(str_n)

#     # Converting string to number
#     num = int(rev)

#     return num




'''
ITERATIVE WAY 

Algorithm:

Input:  num
(1) Initialize rev_num = 0
(2) Loop while num > 0
     (a) Multiply rev_num by 10 and add remainder of num divide by 10 to rev_num
               rev_num = rev_num*10 + num%10;
     (b) Divide num by 10
(3) Return rev_num

'''

def reverseInt(n):
    revNum = 0
    while n > 0:
        revNum = revNum*10 + n % 10
        n = n // 10
    return revNum



num = 1
print(reverseInt(num))