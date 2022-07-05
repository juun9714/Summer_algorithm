import sys

N, M = map(int, sys.stdin.readline().split())
castle=[['.' for _ in range(M)] for _ in range(N)]
for n in range(N):
    castle[n]=list(map(str, sys.stdin.readline().split()))

for n in range(N):
    if 'X' not in castle[n]:
        print("X is not castle[{}]".format(n))
        check=0

        for sero in range(M):
            for garo in range(N):
                if castle[garo][sero]!='X':
                    #print("castle[{}][{}] is empty!! {}".format(garo,sero,castle[garo][sero]))
                    castle[n][sero]='X'
                break
            break
    print(castle)