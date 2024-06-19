# 최소 몇 번 점프해야 오른쪽끝으로 갈 수 있는지 구하기
import collections

n = int(input())
a = list(map(int, input().split()))
d = [float('inf')] * n

queue = collections.deque([])
queue.append(0)
d[0] = 0
while queue:
    node = queue.popleft()
    for i in range(1, a[node] + 1):
        if node + i < n and d[node + i] > d[node] + 1:
            d[node + i] = d[node] + 1
            queue.append(node + i)

print(d[-1] if d[-1] != float('inf') else -1)

