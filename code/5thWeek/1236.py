import sys

N, M = map(int, sys.stdin.readline().split())
castle=[['.' for _ in range(M)] for _ in range(N)]
for n in range(N):
    castle[n]=list(sys.stdin.readline().rstrip())
cnt=0

print("BEFORE")
for q in range(N):
    print(castle[q])

for n in range(N):
    if 'X' not in castle[n]:
        for mm in range(M):
            check=-1
            for nn in range(N):
                if castle[nn][mm]=='X':
                    check=1
                    break
            if(check==-1):
                castle[n][mm]='X'
                cnt+=1
                break

for n in range(N):
    if 'X' not in castle[n]:
        cnt+=1
        castle[n][0]='X'

for m in range(M):
    check2=-1
    for n in range(N):
        if castle[n][m]=='X':
            check2=1
            break
        
    if check2==-1:
        castle[0][m]='X'
        cnt+=1


print("AFTER")
for q in range(N):
    print(castle[q])

print(cnt)