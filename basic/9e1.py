# [최단 경로]
# 1. 간단한 다익스트라 알고리즘
if False:
    import sys
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, c = map(int, input().split()) # 출발, 도착, 비용
        graph[a].append((b, c))

    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                idx = i
        return idx

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost <distance[j[0]]:
                    distance[j[0]] = cost

    dijkstra(start)

    for i in range(1, n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])

# 2. 개선된 다익스트라 알고리즘
if True:
    import heapq
    import sys
    input = sys.stdin.readline
    INF  = int(1e9)

    n, m = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split()) # 출발, 도착, 비용
        graph[a].append((b, c))

    ################### 다른 부분 ###################
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))   # (점으로 가기 위한 거리, 점) ex. (시작점으로 가기 위한 거리는 0, 시작점)
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    ################### 다른 부분 ###################


    dijkstra(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])

'''
input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
output
0
2
3
1
2
4
'''
# 3. 플로이드 워셜 알고리즘
if True:
    INF = int(1e9)

    n = int(input())
    m = int(input())

    graph = [[INF] * (n+1) for _ in range(n + 1)]

    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print("INFINITY", end = ' ')
            else:
                print(graph[a][b], end = ' ')

        print()

