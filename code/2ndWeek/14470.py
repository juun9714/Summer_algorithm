vals=[]
time=0
for _ in range(5):
    vals.append(int(input()))

if vals[0]<0:
    time+=(-1)*vals[0]*vals[2] # 영하~0
    time+=vals[3] # 0 to 0
    time+=vals[1]*vals[4] # 0 to goal
elif vals[0]>0:
    time+=(vals[1]-vals[0])*vals[4]

print(time)