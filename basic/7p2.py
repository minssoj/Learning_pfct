# [이진탐색] 부품 찾기
#========== input ===========
# n : 전체 부품의 개수
# data1 : 전체 부품의 종류
# m : 요청한 부품의 개수
# data2 : 요청한 부품의 종류
#========== output ==========
# result : 요청한 부품이 있으면 각각 yes, no로 표시
# 풀이 : 1) 이진탐색 2) 계수정렬 3) set 사용
# 1) 이진탐색
def BS_v2(array, target, start, end):
    while start <=end:
        mid = (start + end)// 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid +1
    return None

if False:
    n = int(input())
    data1 = list(map(int, input().split()))
    data1.sort()
    m = int(input())
    data2 = list(map(int, input().split()))

    for i in data2:
        result = BS_v2(data1, i, 0, n-1)
        if result != None:
            print("yes", end=' ')
        else:
            print("no", end=' ')

# 2) 계수정렬
if False:
    n = int(input())
    data1 = list(map(int, input().split()))
    m = int(input())
    data2 = list(map(int, input().split()))
    array = [0] * 100000

    for i in data1:
        array[i] = 1

    for i in data2:
        if array[i] == 1:
            print("yes", end=' ')
        else:
            print("no", end=' ')

# 3) set 사용
if True:
    n = int(input())
    data1 = set(map(int, input().split()))
    m = int(input())
    data2 = list(map(int, input().split()))

    for i in data2:
        if i in data1:
            print("yes", end=' ')
        else:
            print("no", end=' ')

'''
input
5
8 3 7 9 2
3
5 7 9
output
no yes yes
'''