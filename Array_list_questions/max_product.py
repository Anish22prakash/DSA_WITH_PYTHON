arr = [1,2,4,9,5]

# approach 1  : by checking all pair of combination one by one 
def max_product(arr):
    Totalmax = arr[0]*arr[1]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(arr[i]*arr[j] > Totalmax ):
                Totalmax = arr[i]*arr[j]
    return Totalmax

print(max_product(arr)) #45

# approach 2 :itrate over array then finding the two largest number and then return the product two values

def max_product2(arr):
    max1 = 0
    max2 = 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2
print(max_product2(arr))  # output: 45


