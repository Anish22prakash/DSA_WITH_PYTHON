# In the code we are running the loop form the 0 to n and print the values , each step takes O(1) time complexity 
# so the overall time complexity is O(n), belwo we are using two loops and we think that the tiem complexity of the code will be O(2n)
# but there is the catch , the overall time complexity is o(n) , because here we are negeleting the constant values
def print_values(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_values(5)


    