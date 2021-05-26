# [다이나믹 프로그래밍] 1로 만들기
#========== input ===========
# n : 정수
#========== output ==========
# result : n을 1로 만들 수 있는 최소의 횟수
# 풀이 : f(n) = min(f(n/5), f(n/3), f(n/2), f(n-1)) + 1
n = int(input())

result = [0] * 30001

for i in range(2, n+1):
    result[i] = result[i-1]+1
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2]+1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3]+1)
    if i % 5 == 0:
        result[i] = min(result[i], result[i//5]+1)
print(result[i])