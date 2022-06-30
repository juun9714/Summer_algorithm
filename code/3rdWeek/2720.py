'''
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오. 
거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
'''
ret=[25,10,5,1]
it=int(input())
out=[[0 for _ in range(4)] for _ in range(it)]
money=[]
for _ in range(it):
    money.append(int(input()))

for j in range(it):
    for i in range(len(ret)):
        out[j][i]=money[j]//ret[i]
        money[j]-=(money[j]//ret[i])*ret[i]

for j in range(it):
    for i in range(len(ret)):
        print(out[j][i], end=' ')
    print("")