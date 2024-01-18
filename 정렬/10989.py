import collections
import sys

a = collections.defaultdict(int)
for _ in range(int(input())):
    a[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(a[i]):
        print(i)
