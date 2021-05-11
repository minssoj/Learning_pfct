# [정렬] 기준에 따라 데이터를 정렬
# 1. 선택정렬 코드 - 시간복잡도 (N^2)
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
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)

# 3. 퀵정렬 - 시간복잡도(NlogN), 최악 (N^2)


# 4. 계수정렬