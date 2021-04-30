# [그리디] 큰 수의 법칙
#========== input ===========
# n : 숫자 목록의 개수
# m : 총 더한 횟수
# k : 최대 반복 횟수
# data : 배열
#========== output ==========
# result : 규칙에 맞게 더했을 때 가장 큰 수
# 풀이 : 가장 큰 수를 최대한 더해보고 그다음으로 큰 수 더하고, 다시 가장 큰 수를 최대한 더 해 본다. 이것을 반복!
# (가장 큰수* k + 두번째 큰수) * m//(k+1) + m%(k+1) * 가장큰수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
l1 = data[-1]
l2 = data[-2]

result = (l1 * k + l2) * (m // (k+1)) + (m % (k+1)) * l1
print(result)



