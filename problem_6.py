def sum_square_difference(num):
    return square_sum(num) - sum_square(num)

def sum_square(num):
    result = 1
    i = 2
    while i <= num:
        result = result + i**2
        i += 1
    return result

def square_sum(num):
    num_list = range(1, num + 1)
    total = sum(num_list)
    return total**2

print(sum_square_difference(100))

#Need to redo because time complexity is too much.  I'm missing a key concept.