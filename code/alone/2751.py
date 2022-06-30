import sys
many=int(sys.stdin.readline())
s_list=[int(sys.stdin.readline()) for _ in range(many)]
for i in sorted(s_list):
    print(i)
