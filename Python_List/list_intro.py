# python list is a data structure that hold an ordered collection of items

import numpy as np

integers =[1,2,3,4,5,5]
print(integers)

strings = ['anish','manish','santosh','enlash']
print(strings)

# updating the list
strings[1] = 'ram'
print(strings)

#itterate using in keyword
for item in strings:
    print(item)

# for inseration we have append and insert funtion 
# in append fucntion we pass only the element , it will append at the ending of the list
# in insert function we pass the index and element both but index is not required if we are inserting
strings.insert(1,'newElement')
strings.append(55)
print(strings)


#for deletion we have three method , 1.pop() ,  2.delete() , 3.remove()
# pop() function will delete the last element of the list , also we can pass the index of element which we have to delete
# delete() function will delete the element at the specified index
# remove() function will take element value and delete the first occurence

myList = [1,34,55,37,67,89,89]
print(myList.pop())
print(myList.pop(0))

del myList[0]
myList.remove(89)
print(myList)

# Slice function 
# slice function is used to get the subset of the list
myList2 = [34,5,1,62,24,53,23]
sliceList = myList2[0:3:2]
print(sliceList)

# searching for the element in a list
my_list = [10,20,30,40,50,60]
target = 500
# using in keyword
if target in my_list:
    print(f"{target} is present in the list")
else:
 print(f"{target} is not present in the list")

# using linear search
def linear_search(lst, target):
    for i in range(len(lst)):
      if lst[i] == target:
        print(f"{target} is present in the list")
        return
    return -1
print(linear_search(my_list, target))
