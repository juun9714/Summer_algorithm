it=int(input())

for _ in range(it):
    H, W, N=map(int,input().split())
    ho=N//H
    flr=N%H

    if flr==0:
        if ho>=10:
            print(str(H)+str(ho))
        else:
            print(str(H)+"0"+str(ho))
    else:
        if ho+1>=10:
            print(str(flr)+str(ho+1))
        else:
            print(str(flr)+"0"+str(ho+1))
