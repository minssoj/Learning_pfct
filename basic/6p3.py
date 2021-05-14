# [정렬] 성적이 낮은 순서로 학생 출력하기
#========== input ===========
# n : 학생 수
# data : (학생이름, 점수)로 구성
#========== output ==========
# result : 점수 낮은 순으로 이름 출력
# 풀이 : Python 내장함수에서 key 사용

n = int(input())

data = []
for i in range(n):
    temp = input().split()
    data.append((temp[0], int(temp[1])))

results = sorted(data, key=lambda student:student[1])

for result in results:
    print(result[0], end=' ')