import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
movable = [float('inf')] * (n + 1)
for _ in range(e):
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))
start, end = map(int, input().split())

heap = []
heapq.heappush(heap, (-float('inf'), start))

while heap:
    w, node = heapq.heappop(heap)
    w = -w

    if movable[node] < float('inf'):
        continue

    movable[node] = w
    for next_node, weight in graph[node]:
        if movable[next_node] == float('inf'):
            heapq.heappush(heap, (-min(weight, w), next_node))

print(movable[end])
