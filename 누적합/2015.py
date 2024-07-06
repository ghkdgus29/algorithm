import collections

n, target = map(int, input().split())
a = list(map(int, input().split()))
counter = collections.defaultdict(int)
counter[0] = 1
prefix_sum = 0
ans = 0
for val in a:
    prefix_sum += val
    if prefix_sum - target in counter:
        ans += counter[prefix_sum - target]

    counter[prefix_sum] += 1

print(ans)
