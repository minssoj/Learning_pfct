# [구현] 시각
#========== input ===========
# n : 특정시각
#========== output ==========
# result :  00:00:00 ~ n:59:59 까지 3이 한 번 이상 포함되는 경우의 수
# 풀이 :
n = int(input())
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            t = str(h)+str(m)+str(s)
            if '3' in t:
                result += 1
print(result)