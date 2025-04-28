# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24
import math as mat
def sum_product(input_tuple):
    total_sum = sum(input_tuple)
    total_product = mat.prod(input_tuple)
    print(total_sum,total_product)

sum_product((1,2,3,4))