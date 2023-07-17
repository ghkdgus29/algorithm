import collections

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)

for _ in range(n - 1):
    n1, n2 = map(int, input().split())

    graph[n1].append(n2)
    graph[n2].append(n1)

queue = collections.deque([1])
parent[1] = 0

while queue:
    node = queue.popleft()

    for i in graph[node]:
        if parent[i] == -1:
            parent[i] = node
            queue.append(i)

print(*parent[2:], sep="\n")
