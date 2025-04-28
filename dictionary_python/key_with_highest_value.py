# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output: b

#solution one
def max_value_key(my_dict):
    intmax =  0
    result = ''
    for key,values  in my_dict.items():
        if values > intmax :
            intmax = values
            result = key
    return result

#solution two

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(my_dict))

my_dict2 = {'a': 5, 'b': 9, 'c': 2}

print('a' in my_dict2)