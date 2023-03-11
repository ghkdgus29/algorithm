import collections

node_cnt, edge_cnt, start = map(int, input().split())

graph = [[] for _ in range(node_cnt + 1)]
visit = [False] * (node_cnt + 1)

for _ in range(edge_cnt):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for line in graph:          # 그래프 탐색 순서때매 정렬
    line.sort()


def dfs(node):
    visit[node] = True
    print(node, end=" ")

    for i in graph[node]:
        if not visit[i]:
            dfs(i)


def bfs(node):
    queue = collections.deque([node])
    visit[node] = True

    while queue:
        fivot = queue.popleft()
        print(fivot, end=" ")

        for i in graph[fivot]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


dfs(start)
print()
visit = [False] * (node_cnt + 1)
bfs(start)
