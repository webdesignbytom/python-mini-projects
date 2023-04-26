# Array functions

## Find the sum of an array

def _sum(arr):
    sum = 0
    
    for i in arr:
        sum = sum + i
    
    return sum

    # input values to list
arr = [12, 3, 4, 15]
 
    # calculating length of array
n = len(arr)
    # calling function ans store the sum in ans
ans = _sum(arr)
    # display sum
print('Sum of the array is ', ans)
    