# [이진탐색] 떡볶이 떡 만들기
#========== input ===========
# n : 떡의 개수
# m : 요청한 떡의 길이
# l : 떡의 길이들
#========== output ==========
# result : 손님이 적어도 m만큼의 떡을 가지고 가기 위한 높이의 최댓값
# 풀이 : 이진탐색
n, m = list(map(int, input().split(' ')))
l = list(map(int, input().split()))

# 이진탐색 변수 선언
start = 0
end = max(l)

result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    
    # 이진탐색의 기준인 모인 떡의 길이
    for length in l:
        if length>mid:
            total += length -mid
    
    # 이진탐색
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)