import collections

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n):
    given = list(map(int, input().split()))

    fivot_node = given[0]

    given = given[1:-1]

    for idx in range(0, len(given), 2):
        node = given[idx]
        weight = given[idx + 1]

        graph[fivot_node].append((node, weight))

dist = [-1] * (n + 1)


def bfs(start):
    dist[start] = 0
    queue = collections.deque([start])

    while queue:
        current_node = queue.popleft()

        for node, weight in graph[current_node]:
            if dist[node] == -1:
                dist[node] = dist[current_node] + weight
                queue.append(node)


bfs(1)
start = dist.index(max(dist))

dist = [-1] * (n + 1)
bfs(start)
print(max(dist))
