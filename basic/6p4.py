# [정렬] 두 배열의 원소 교체
#========== input ===========
# N : 배열의 길이
# k : 교체 횟수
# data : 두개의 배열
#========== output ==========
# result : A 배열의 모든 원소의 합의 최대값
# 풀이 : Python 내장함수 sort 사용
N, k = map(int, input().split())
data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))

data_1.sort()
data_2.sort(reverse=True)

for i in range(k):
    if data_1[i] < data_2[i]:
        data_1[i], data_2[i] = data_2[i], data_1[i]
    else:
        break

print(sum(data_1))