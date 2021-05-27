# [다이나믹 프로그래밍] 개미 전사
#========== input ===========
# n : 식량창고의 개수
#========== output ==========
# result : n을 1로 만들 수 있는 최소의 횟수
# 풀이 : f(n) = min(f(n-1), f(n-2)+ n번째의 식량)
n = int(input())
food = list(map(int, input().split()))

result = [0] * 100

result[0] = food[0]
result[1] = max(food[0], food[1])
for i in range(2, n):
    result[i] = max(result[i-1], result[i-2]+food[i])
print(result[n-1])