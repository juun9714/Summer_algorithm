# 초콜릿 자르기
import sys

N,M=map(int, sys.stdin.readline().split())

cum=0
pieces=1

while pieces!=N*M:
    cum+=1
    pieces+=1
print(cum)


