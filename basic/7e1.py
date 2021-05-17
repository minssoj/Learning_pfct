# [이진 탐색] 범위를 반씩 좁혀가는 탐색
# 1. 순차 탐색
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

'''
input:
5 DB
HN JG DB TI SW
output:
3
'''
# 2. 이진 탐색
# 2-1. 재귀함수



# 2-2. 반복문



# 기타. 한줄로 입력 받기