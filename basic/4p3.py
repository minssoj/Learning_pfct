# [구현] 게임 개발
#========== input ===========
# N : 행의 개수
# M : 열의 개수
# y, x, d : 캐릭터의 위치와 방향
# data : 맵의 상태 (육지 or 바다)
#========== output ==========
# result : 캐릭터가 방문한 칸 의 수
# 풀이 : 주어진 조건 그대로 구현, 시뮬레이션 (책참고)
N, M = map(int, input().split())
y, x, d = map(int, input().split())     # y, x좌표, 방향
check = [[0]*M for _ in range(N)]
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

check[y][x] = 1
result = 1

# 0: 북, 1:동, 2:남, 3:서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

turn_num = 0

while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]

    if check[ny][nx] == 0 and data[ny][nx] == 0:
        check[ny][nx] = 1
        x = nx
        y = ny
        result += 1
        turn_num = 0
        continue
    else:   # 돌기시작
        turn_num += 1

    if turn_num == 4: # 다 돌았을 경우
        nx = x - dx[d]
        ny = y - dy[d]

        if data[ny][nx] == 0:
            x = nx
            y = ny

        else:
            break
        turn_num = 0

print(result)
