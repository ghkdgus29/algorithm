import collections
import sys

a = collections.defaultdict(int)

for _ in range(int(input())):
    a[int(sys.stdin.readline())] += 1


max_cnt = -1
ans = -1
for key in sorted(a.keys()):
    if max_cnt < a[key]:
        ans = key
        max_cnt = a[key]

print(ans)
