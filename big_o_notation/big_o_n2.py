# here in the code the time complexity is n^2 , we are using nested loop ,
# the first itteration the second loop will run from 0 to n , in the similar way , for nth itteration the second loop 
# will run from 0 to n . so overall time complexity will be O(n^2)
def print_values(n):
    for i in range(n):
        for j in range(n):
         print(i,j)

print_values(5)