# [다이나믹 프로그래밍] 효율적인 화폐 구성
#========== input ===========
# n : 화폐의 가지 수
# m : 가치의 합
# data : 화폐의 종류
#========== output ==========
# result : 경우의 수, 불가능하면 -1출력
# 풀이 : f(n) = min(f(n), f(n-화폐단위)+1)

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

result = [10001] * (m+1)

result[0] = 0
for i in range(n):
    for j in range(data[i], m+1):
        if result[j-data[i]] != 10001:
            result[j] = min(result[j], result[j-data[i]]+1)

if result[m] == 10001:
    print(-1)
else:
    print(result[m])
