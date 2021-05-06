# [DFS/BFS] 미로 탈출
#========== input ===========
# N : 행의 개수
# M : 열의 개수
# data : 얼음틀
#========== output ==========
# result : 틀 안의 아이스크림 수
# 풀이 :  BFS 진행 (N, M) 방문하면 종료
from collections import deque

N, M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input())))

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        # 경우의 수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if data[ny][nx] == 0:
                continue
            elif data[ny][nx] == 1:
                data[ny][nx] = data[y][x] +1
                q.append((nx, ny))
    return data[N-1][M-1]

print(BFS(0, 0))

# 테스트케이스
'''
input
5 6
101010
111111
000001
111111
111111
output
10
'''