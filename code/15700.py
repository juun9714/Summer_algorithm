N,M=map(int,(input().split()))

total=0

if N==1 and M==1:
    total=0
elif N==1 and M!=1:
    total=M//2
elif N!=1 and M==1:
    total=N//2
elif N%2==0:
    total=(N//2)*M
elif N%2!=0 and M%2==0:
    total=(M//2)*N
elif N%2!=0 and M%2!=0:
    total=(N//2)*M+(M//2)

print(int(total))