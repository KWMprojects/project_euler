def largest_palindrome_product(num):
    highest_num = 9 * (int('1' * num))
    lowest_num = int('1' + ('0' * (num - 1)))
    print(highest_num, lowest_num)
    max_product = 0
    for i in range(highest_num, lowest_num - 1, -1):
        for j in range(i, lowest_num - 1, -1):
            product = i * j
            product_string = str(product)
            if product_string == ''.join(reversed(product_string)) and product > max_product:
                max_product = product
    return max_product


print(largest_palindrome_product(3))
            
