from functools import reduce # Learned to use a new function (kinda like map in JS)

def smallest_multiple(*args):
    return reduce(lcm, args)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


print(smallest_multiple(*range(1, 20)))