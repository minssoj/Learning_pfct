# [DFS/BFS] 꼭 필요한 자료구조 기초
## 1. Stack (List로 구현)
stack =  []

stack.append(5) # 삽입
stack.append(2) # 삽입
stack.append(3) # 삽입
stack.append(7) # 삽입
stack.pop()     # 삭제
stack.append(1) # 삽입
stack.append(4) # 삽입
stack.pop()     # 삭제
print(stack)

## 2. Queue (deque로 구현)
from collections import deque

queue = deque()

queue.append(5)     # 삽입
queue.append(2)     # 삽입
queue.append(3)     # 삽입
queue.append(7)     # 삽입
queue.popleft()     # 삭제
queue.append(1)     # 삽입
queue.append(4)     # 삽입
queue.popleft()     # 삭제
print(queue)
queue.reverse()
print(queue)
print(list(queue))  # 리스트로 변환

## 3. 재귀함수의 예시 (팩토리얼)
# 재귀함수의 경우 메모리에서 스택 구조 형태로...
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recur(n):
    if n <= 1:
        return 1
    return n * factorial_recur(n-1)

print(factorial_iter(5))
print(factorial_recur(5))