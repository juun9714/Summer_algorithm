arr=[tmp for tmp in range(1,10001)]
for start in range(1,10001):
    selfNum=start

    for i in range(len(str(start))):
        selfNum+=int(str(start)[i])


    if selfNum in arr:
        arr.remove(selfNum)


for i in range(len(arr)):
    print(arr[i])