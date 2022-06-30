snack=[0 for _ in range(3)]

for i in range(3):
    P, W=map(int,(input().split()))
    if P*10>=5000:
        snack[i]=(W*10)/((P*10)-500)
    else:
        snack[i]=(W*10)/(P*10)
    
if snack.index(max(snack))==0:
    print("S")
elif snack.index(max(snack))==1:
    print("N")
else:
    print("U")
