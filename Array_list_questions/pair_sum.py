
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


def pair_sum(myList, sum):
    result =[]
    i = 0
    while i < len(myList):
        j = len(myList) - 1 
        while i < j :
            if myList[i]+myList[j] == sum:
                result.append(f'{myList[i]}+{myList[j]}')
            j -=1
        i +=1
    return result
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))