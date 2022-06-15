N,M=map(int, input().split())
grid=[]

for i in range(N):
    grid_tmp=list(map(int,input().split()))
    grid.append(grid_tmp)
print(grid)

#https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=411
'''
외부 공기 유입 가능
    - 격자의 맨 가장 자리는 얼음이 놓이지 않음. 
    - 즉, 격자의 맨 가장자리에서 목표 얼음까지 도달 가능하면 닿아있는 것임
    - 두 개 이상의 box에 외부 공기가 유입 가능해야 함
        - (1,1) box에서 주변 box 4개 중 2개 이상의 box를 목적지로 한 경로가 존재하면 해동 가능함
    
'''