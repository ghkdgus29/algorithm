import sys


def dfs(depth, visit_node):
    if depth == 4:
        print(1)
        sys.exit(0)

    check[visit_node] = True        # 방문 체크

    for i in graph[visit_node]:
        if not check[i]:
            dfs(depth + 1, i)

    check[visit_node] = False       # 방문 초기화


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
check = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):      # 모든 노드에 대해 DFS
    dfs(0, i)

print(0)
