# implementation of array using array module and numpy module
import array
import numpy as np

arr = array.array('i');  # declaration 
arr.append(1);  # initialization
print(arr)


arr1 = array.array('i' ,[1,2,3,4,5]);  # declaration and initialization
print(arr1);



numpy_array = np.array([],dtype=int)
numpy_array = np.append(numpy_array, 1)  # append method insert the element in the array from the end
print(numpy_array)

arr2 = np.array([1,2,3,4,5]);

# traversing the linear array
td_Array = array.array('i',[]);

n = int(input("how many elements do you want to store in the array : "))
for i in range(n):
    element = int(input(f"enter the element{i+1} : "))
    td_Array.append(element)

print("The elements in the array are:")

def traverse(array):
    for i in range(len(array)):
        print(array[i],end=" ")

traverse(td_Array)


# searching the element in the linear array 
def search(array, target):
    for i in range(n):
        if(array[i]== target):
            return "found foun found !!!"
    return "target not found"
search(td_Array , 67)

# deleting the element from the array 
loc = int(input("enter the location/ index which you want to delete the element : "))
def delete_Array (array,loc):
    if loc < 0 and  loc >= len(array):
        return "invalid index"
    else:
        index = array.pop(loc)
        return "element deleted successfully"
    
delete_Array(td_Array, loc)
print(td_Array)




