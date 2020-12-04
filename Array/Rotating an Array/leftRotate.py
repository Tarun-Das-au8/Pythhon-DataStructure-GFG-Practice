def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1


def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    print(arr)


def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end='')


arr = []
n = int(input('Enter the elements you want in array : '))
for _ in range(n):
    num = int(input())
    arr.append(num)

d = int(input("Enter rotation value : "))

leftRotate(arr, d)
# printArray(arr)
