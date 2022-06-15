avg=0
for _ in range(5):
    tmp=int(input())
    if tmp<40:
        avg+=40
    else:
        avg+=tmp
print(avg//5)