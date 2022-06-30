import sys
num=int(sys.stdin.readline())
for _ in range(num):
    score=sys.stdin.readline()
    cum=1
    total=0
    for sc in score:
        if sc=="O":
            total+=cum
            cum+=1
        else:
            cum=1
    print(total)