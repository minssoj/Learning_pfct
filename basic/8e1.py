# [다이나믹 프로그래밍]
# 1. 피보나치 함수 소스코드
def fibo_v1(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo_v1(x - 1) + fibo_v1(x - 2)
print(fibo_v1(4))

# 2. 피보나치 수열 소스코드 (재귀적)
result = [0] * 100
def fibo_v2(x):
    if x == 1 or x == 2:
        return 1
    if result[x] != 0:
        return result[x]
    result[x] = fibo_v2(x-1) + fibo_v2(x-2)
    return result[x]
print(fibo_v2(99))

# 3. 호출되는 함수 확인
result = [0] * 100
def fibo_v3(x):
    print('f(' + str(x) + ')', end= ' ')
    if x == 1 or x == 2:
        return 1
    if result[x] != 0:
        return result[x]
    result[x] = fibo_v3(x-1) + fibo_v3(x-2)
    return result[x]
fibo_v3(6)
print()

# 4. 피보나치 수열 소스코드 (반복적)
result = [0] * 100

result[1] = 1
result[2] = 1
n = 99

for i in range(3, n+1):
    result[i] = result[i - 1] + result[i - 2]
print(result[n])