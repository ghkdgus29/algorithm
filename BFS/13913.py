import collections

MAX = 100000

soobin, younger = map(int, input().split())

distance = [0] * (MAX + 1)
visit = [False] * (MAX + 1)
parent = [-1] * (MAX + 1)                   # 역추적을 하기 위해 부모 노드를 저장

visit[soobin] = True
queue = collections.deque([soobin])

while queue:
    current_loc = queue.popleft()

    if current_loc > 0:
        if not visit[current_loc - 1]:
            visit[current_loc - 1] = True
            distance[current_loc - 1] = distance[current_loc] + 1
            parent[current_loc - 1] = current_loc
            queue.append(current_loc - 1)

    if current_loc < MAX:
        if not visit[current_loc + 1]:
            visit[current_loc + 1] = True
            distance[current_loc + 1] = distance[current_loc] + 1
            parent[current_loc + 1] = current_loc
            queue.append(current_loc + 1)

    if current_loc * 2 <= MAX:
        if not visit[current_loc * 2]:
            visit[current_loc * 2] = True
            distance[current_loc * 2] = distance[current_loc] + 1
            parent[current_loc * 2] = current_loc
            queue.append(current_loc * 2)

print(distance[younger])

path = []

current_idx = younger
while current_idx != -1:
    path.append(current_idx)
    current_idx = parent[current_idx]

print(*reversed(path))
