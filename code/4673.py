start=1
arr=[tmp for tmp in range(10000)]
print(arr)
while True:
    selfNum=start
    for i in range(len(str(start))):
        selfNum+=int(str(start)[i])
    if selfNum>9999:
        break
    else:
        print(selfNum)
        if selfNum in arr:
            arr.remove(selfNum)
        start+=1


#for p in range(len(arr)):
    #print(arr[p])

# A=3345
# selfNum=A
# for i in range(len(str(A))):
#     print(int(str(A)[i]))
#     selfNum+=int(str(A)[i])
# print(selfNum)