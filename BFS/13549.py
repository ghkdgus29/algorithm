import collections

soob, bro = map(int, input().split())

NOT_VISIT = 200000
dist = [NOT_VISIT] * 100001

queue = collections.deque([soob])
dist[soob] = 0

while queue:
    pos = queue.popleft()

    if pos * 2 < 100001 and dist[pos * 2] > dist[pos]:
        dist[pos * 2] = dist[pos]
        queue.append(pos * 2)

    if pos + 1 < 100001 and dist[pos + 1] > dist[pos] + 1:
        dist[pos + 1] = dist[pos] + 1
        queue.append(pos + 1)

    if pos - 1 >= 0 and dist[pos - 1] > dist[pos] + 1:
        dist[pos - 1] = dist[pos] + 1
        queue.append(pos - 1)

print(dist[bro])
