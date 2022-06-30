import sys

while True:
    text=sys.stdin.readline()
    if text=='':
        break

    out=[0 for _ in range(4)]
    for i in text:
        if i.islower():
            out[0]+=1
        elif i.isupper():
            out[1]+=1
        elif i.isdigit():
            out[2]+=1
        elif i==' ':
            out[3]+=1
        else:
            continue

    print('{} {} {} {}'.format(out[0],out[1],out[2],out[3]))
