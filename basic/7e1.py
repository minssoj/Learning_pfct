# [이진 탐색] 범위를 반씩 좁혀가는 탐색
# 1. 순차 탐색
def SS(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

if False:
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
    input_data = input().split()
    n = int(input_data[0])
    target = input_data[1]

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = input().split()

    print(SS(n, target, array))

'''
input:
5 DB
HN JG DB TI SW
output:
3
'''
# 2. 이진 탐색
# 2-1. 재귀함수
def BS(array, target, start, end):
    if start > end:
        return None
    # 1. 중간 점 찾기
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif  array[mid] > target:
        return BS(array, target, start, mid-1)
    else:
        return BS(array, target, mid+1, end)

# 2-2. 반복문
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

if True:
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = BS_v2(array, target, 0, n-1)
    if result == None:
        print("Not exist")
    else:
        print(result+1)
'''
input:
10 7
1 3 5 7 9 11 13 15 17 19
output:
4
'''
# 기타. 한줄로 입력 받기
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)