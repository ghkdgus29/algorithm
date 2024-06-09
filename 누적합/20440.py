import collections
import sys

n = int(input())
start = []
end = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    start.append(s)
    end.append(e)

start.sort()
end.sort()

timeline = collections.defaultdict(int)
for s in start:
    timeline[s] += 1
for e in end:
    timeline[e] -= 1
    if timeline[e] == 0:
        del timeline[e]

points = sorted(timeline.keys())
for i in range(1, len(points)):
    timeline[points[i]] += timeline[points[i - 1]]

s = e = 0
max_val = 0
for idx, p in enumerate(points):
    if timeline[p] > max_val:
        s = p
        e = points[idx + 1]
        max_val = timeline[p]

print(max_val)
print(s, e)
