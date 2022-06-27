import sys

num=int(sys.stdin.readline())
ppl=[[1 for _ in range(3)] for _ in range(num)]

for i in range(num):
    tmp=list(map(int, sys.stdin.readline().split()))
    ppl[i][0]=tmp[0]
    ppl[i][1]=tmp[1]

for p in range(num):
    for q in range(num):
        if p!=q and ppl[p][0]<ppl[q][0] and ppl[p][1]<ppl[q][1]:
            ppl[p][2]+=1

for a in ppl:
    print(a[2], end=' ')