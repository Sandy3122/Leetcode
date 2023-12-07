'''
Count Number Of Factorial In N
'''

def factorialCount(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n//i == i:
                count += 1
            else:
                count += 2
    return count

print(factorialCount(36))
