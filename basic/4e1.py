# [구현] 상하좌우
#========== input ===========
# n : map 크기 (n by n)
# D : 이동 방향
#========== output ==========
# result : 도착 위치
# 풀이 : 방향에 따라 위치 업데이트
n = int(input())
D = input().split()

D_list = ['L', 'R', 'U', 'D']
dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]

x = 1
y = 1
for d in D:
    for i in range(4):
        if d == D_list[i]:
            nx = x +dx[i]
            ny = y +dy[i]

    if nx <1 or ny <1 or nx>n or ny>n:
        continue
    x = nx
    y = ny
print(x, y)
