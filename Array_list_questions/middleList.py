arr = [1,2,3,4]
def middle(lst):
    n= len(lst)
    result = lst[1:n-1:1]
    return result
print(middle(arr))