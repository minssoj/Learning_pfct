# [정렬] 기준에 따라 데이터를 정렬
# 1. 선택정렬 코드 - 시간복잡도 (N^2)
print("========== 선택정렬 ==========")
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

# 기타. 파이썬 스와이프
array = [3, 5]
array[0], array[1] = array[1], array[0]

# 2. 삽입정렬 코드 - 시간복잡도 (N^2), 최선 (N)
print("========== 삽입정렬 ==========")
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)

# 3. 퀵정렬 - 시간복잡도(NlogN), 최악 (N^2)
# version 1
print("========== 퀵정렬 ==========")
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left]<= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            left -= 1
        if left >right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)

# version 2
print("========== 퀵정렬 v2 ==========")
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort_v2(array):
    if len(array)<= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_v2(left_side) + [pivot] + quick_sort_v2(right_side)

print(quick_sort_v2(array))

# 4. 계수정렬 - 시간복잡도 (N+K) : K는 행렬의 최대값
print("========== 계수정렬 ==========")
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
print()

# 기타. Python 정렬 내장함수
# sorted
print("========== sorted ==========")
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)

# sort
print("========== sort ==========")
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array)

# sort 내 key인자 활용
array = [('banana', 2), ('apple', 5), ('carrot', 3)]
def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)