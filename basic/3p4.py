# [그리디] 1이 될 때까지
#========== input ===========
# n : 최초의 수
# k : 나누는 수 (나누어 떨어질 때만)
#========== output ==========
# result : N-1 or N/K를 반복하여 1을 만들 수 있는 최소의 횟수
# 풀이 : 당연히 나누는 것이 1에 빨리 다가갈 수 있다.
# '수가 k의 배수가 아니면 k의 배수가 되도록 1씩 빼주고 k로 나눈다' 를 반복

n, k = map(int, input().split())
result = 0

# ===== 풀이 =====
while n != 1:
    if n % k == 0:
        result += 1
        n = n // k
    else:
        result += (n % k)
        n = n // k
print(result)