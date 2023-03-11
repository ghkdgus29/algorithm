import sys
sys.setrecursionlimit(10 ** 6)


def dfs(i, team):
    visit[i] = team

    for j in graph[i]:
        if visit[j] == 0:
            dfs(j, 3 - team)


t = int(input())

for _ in range(t):
    node, edge = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node + 1)]
    visit = [0] * (node + 1)
    for _ in range(edge):
        a, b = map(int, sys.stdin.readline().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, node + 1):
        if visit[i] == 0:
            dfs(i, 1)

    bin_graph = True
    for i in range(1, node+1):
        for j in graph[i]:
            if visit[i] == visit[j]:
                bin_graph = False

    print("YES" if bin_graph else "NO")
