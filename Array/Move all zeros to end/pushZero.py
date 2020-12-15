# Function to move all zeros present in the list to the end
def pushZero(arr):
    # count stores index of next available position
    count = 0
    # do for each element
    for i in arr:
        # if current element is non-zero, put the element at
        # next free position in the list
        if i:
            arr[count] = i
            count += 1
 
    # move all 0's to the end of the list (remaining indices)
    for i in range(count, len(arr)):
        arr[i] = 0

    return arr
 
arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
print(pushZero(arr))
 