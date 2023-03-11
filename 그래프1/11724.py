node_cnt, edge_cnt = map(int, input().split())

graph = [[] for _ in range(node_cnt + 1)]
visit = [False] * (node_cnt + 1)

for _ in range(edge_cnt):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visit[node] = True

    for i in graph[node]:
        if not visit[i]:
            dfs(i)


cnt = 0
for i in range(1, node_cnt + 1):
    if not visit[i]:
        dfs(i)
        cnt += 1

print(cnt)
