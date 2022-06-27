import sys
num=int(sys.stdin.readline())
point=[list(map(int, sys.stdin.readline().split())) for _ in range(num)]

for i in sorted(point, key=lambda x:(x[0],x[1])):
    print(i[0], i[1])