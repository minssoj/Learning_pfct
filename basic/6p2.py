# [정렬] 위에서 아래로
#========== input ===========
# n : 입력 받을 수의 개수
# data : 정렬하고 싶은 수들
#========== output ==========
# result : 내림차순으로 정렬
# 풀이 :  파이썬 내장 함수 사용
n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

result = sorted(data, reverse=True)

for i in result:
    print(i, end= ' ')