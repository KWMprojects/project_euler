from math import sqrt

def prime_factorization(num):
    factors = []
    while num % 2 == 0:
        num = num / 2
        factors.append(2)
    
    #Every composite number has at least one prime factor less than or equal to the square root of itself.
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            num = num / i
            factors.append(i)
    
    if num > 2:
        factors.append(num)

    return max(factors)


print(prime_factorization(600851475143))

