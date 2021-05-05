# [DFS/BFS] 음료수 얼려 먹기
#========== input ===========
# N : 행의 개수
# M : 열의 개수
# data : 얼음틀
#========== output ==========
# result : 틀 안의 아이스크림 수
# 풀이 :  DFS 반복

N, M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, input())))
result = 0

def DFS(x, y):
    if x<0 or x>=M or y<0 or y>=N:
        return False
    if data[y][x] == 0:
        # 단지 번호 매기기 문제에서는 단지 번호를 넣어준다.
        data[y][x] = 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if DFS(j, i) == True:
            result += 1

print(result)

# 테스트 케이스
'''
input
4 5
00110
00011
11111
00000
output
3
'''