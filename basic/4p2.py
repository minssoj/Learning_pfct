# [구현] 왕실의 나이트
#========== input ===========
# l : 현재 위치
#========== output ==========
# result :  나이트가 갈 수 있는 경우의 수
# 풀이 : 모든 경우에 대하여 계산해보고, result 1 증가
l = input()
result = 0

# 현재 위치 숫자로 변환
row = int(l[1])
col = int(ord(l[0])) -int(ord('a')) + 1
# 모든 이동 경우의 수
move_list = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for m in move_list:
    y = row + m[0]
    x = col + m[1]

    if y>8 or y<1 or x>8 or x<1:
        continue
    result += 1
print(result)