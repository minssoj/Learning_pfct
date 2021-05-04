# [DFS/BFS] 탐색 알고리즘 DFS/BFS
# 6. 인접 행렬 방식
INF = 999999999
graph_m = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph_m)

# 7. 인접 리스트 방식
num_node = 3
graph_l = [[] for _ in range(num_node)]
graph_l[0].append((1, 7))
graph_l[0].append((2, 5))
graph_l[1].append((0, 7))
graph_l[2].append((0, 5))
print(graph_l)

# 8. DFS - 스택, 재귀함수
# 1 ~ 8 node
def dfs(graph, v, visited):     # v: 시작 노드
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph_dfs = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
dfs(graph_dfs, 1, visited)
print("\ndfs end")

# 9. BFS- 큐
# deque 사용하는 것이 좋음
# 일반적으로 DFS보다 빠름
from collections import deque
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
graph_bfs = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
bfs(graph_bfs, 1, visited)
print("\nbfs end")