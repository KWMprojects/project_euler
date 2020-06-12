def sum_square_difference(num):
    return sum_square(num) - square_sum(num)

def sum_square(num):
    result = 1
    i = 2
    while i <= num:
        result = result + i**2
    return result

def square_sum(num):
    num_list = range(1, num + 1)
    total = sum(num_list)
    return total**2

print(sum_square_difference(10))
        