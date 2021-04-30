# [그리디] 숫자 카드 게임
#========== input ===========
# n : 행의 개수
# m : 열의 개수
# data : 값 (행단위)
#========== output ==========
# result : 행의 가장 작은수를 뽑았을 때, 그 중 가장 큰 수
# 풀이 : max(행별로 최솟값)

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)