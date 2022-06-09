full=[1,1,2,2,2,8]
list=input().split()

for i in range(6):
    full[i]-=int(list[i])
    print(full[i], end=' ')