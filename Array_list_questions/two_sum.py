# two sum problem
# input is arr =  [1,3,4,5] and target = 9  , output = [2,3]

arr =[2,7,11,15]
target = 17

def two_sum(arr, target):
    i = 0
    j = len(arr) - 1
    result =[]
    while(i<j):
        if(arr[i] + arr[j] == target):
         result.append([i,j])
         break
        elif(arr[i] + arr[j] < target):
           i += 1
        else:
           j -= 1
    return result

print(two_sum(arr,target))
   