def RotateArray(arr,d):
	l = len(arr)
	for _ in range(d):
		temp = arr[0]
		for i in range(l-1):
			arr[i] = arr[i+1]
		arr[l-1] = temp
	print(arr)

arr = []
T = int(input("Test Cases : "))
N,d = map(int,input().split())

for _ in range(T):
    for _ in range(N):
        num = int(input())
        arr.append(num)

RotateArray(arr, d);

# def RotateArray(arr,d):
# 	l = len(arr)
# 	for _ in range(d):
# 		temp = arr[0]
# 		for i in range(l-1):
# 			arr[i] = arr[i+1]
# 		arr[l-1] = temp
# 	print(arr)

# arr = []
# T = int(input())
# N,d = map(int,input().split())

# for _ in range(T):
#     arr = list(map(int,input().split())

# RotateArray(arr, d)
    