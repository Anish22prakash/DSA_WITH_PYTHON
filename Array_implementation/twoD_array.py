# implementation of two dimensional array
import numpy as np

td_array = np.array([[5,65,38,98],[86,4,65,32],[56,32,76,12],[36,98,24,72]])
print(td_array)

# travesal of two dimensional array
def  traverse_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traverse_array(td_array)

# searching an element in the two dimensional array using linear search 
def  linear_search(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return f"Element {target} found at position [{i}][{j}]"
    return "Not found"

print(linear_search(td_array, 98))

#delete an element in the two dimensional array
print()
print("delete an element in the two dimensional array ")
print()
def delete_element(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        return "Invalid index"
    else :
        step1 = np.delete(array,rowIndex, axis=0)
        result = np.delete(step1,colIndex,axis=1)
    return result

print(delete_element(td_array,1,0))
