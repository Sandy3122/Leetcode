# Check Is Prime Or Not

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
        
# print(isPrime(2))




# Print N prime numbers



def generatePrimes(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        isPrime = True
        for i in range(len(primes)):
            if num % primes[i] == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
        num += 2
    return primes

print(generatePrimes(10))