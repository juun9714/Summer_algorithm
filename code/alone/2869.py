# 달팽이는 올라가고 싶다
import sys

a,b,v=map(int, sys.stdin.readline().split())
k=(v-b)/(a-b)
print(int(k) if int(k)==k else int(k)+1)

# if k==int(k):
#     print(int(k))
# else:
#     print(int(k)+1)

# 결국 검색 함