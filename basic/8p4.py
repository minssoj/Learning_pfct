# [다이나믹 프로그래밍] 바닥 공사
#========== input ===========
# n : 가로 길이
#========== output ==========
# result : 바닥을 채우는 경우의 수
# 풀이 : f(n) = f(n-1) + 2 * f(n-2)
n = int(input())

result = [0] * 1001

result[1] = 1
result[2] = 3

for i in range(3, n+1):
    result[i] = (result[i-1] + 2 * result[i-2]) % 796796

print(result[n])