import sys

num=int(sys.stdin.readline())
arr=[0 for _ in range(10001)]

for i in range(num):
    arr[int(sys.stdin.readline())]+=1

for j in range(10001):
    if arr[j]>0:
        for jj in range(arr[j]):
            print(j)

# 메모리 초과!!!!!!