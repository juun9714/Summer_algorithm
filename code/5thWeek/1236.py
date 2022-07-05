import sys

N, M = map(int, sys.stdin.readline().split())
castle=[['.' for _ in range(M)] for _ in range(N)]
for n in range(N):
    castle[n]=list(sys.stdin.readline().rstrip())
print(castle)
for n in range(N):
    if 'X' not in castle[n]:
        print("X is not castle[{}]".format(n))
        for mm in range(M):
            check=-1
            for nn in range(N):
                if castle[nn][mm]=='X':
                    check=1
                    break
            if(check==-1):
                print("check is {} and X is added to castle[{}][{}]".format(check,n,mm))
                castle[n][mm]='X'
                break

for n in range(N):
    if 'X' not in castle[n]:
        print("X is added to castle[{}][{}]".format(n,0))
        castle[n][0]='X'


print(castle)