import collections

total, current_floor, target_floor, up, down = map(int, input().split())

NOT_VISIT = -1
dist = [NOT_VISIT] * (total + 1)
queue = collections.deque()

dist[current_floor] = 0
queue.append(current_floor)
while queue:
    cur = queue.popleft()

    if cur + up <= total and dist[cur + up] == NOT_VISIT:
        dist[cur + up] = dist[cur] + 1
        queue.append((cur + up))

    if cur - down > 0 and dist[cur - down] == NOT_VISIT:
        dist[cur - down] = dist[cur] + 1
        queue.append((cur - down))

print(dist[target_floor] if dist[target_floor] != NOT_VISIT else 'use the stairs')
