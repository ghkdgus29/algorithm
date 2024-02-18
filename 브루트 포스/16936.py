import collections

n = int(input())
nums = list(map(int, input().split()))
nums_set = set(nums)
counter = collections.defaultdict(list)

start = float('inf')
cnt_3 = 0
max_idx = -1
for each in nums:
    idx = 0
    num = each
    while num % 3 == 0:
        num //= 3
        idx += 1

    max_idx = max(idx, max_idx)
    counter[idx].append(each)

for key in counter.keys():
    counter[key].sort()


while max_idx >= 0:
    if max_idx in counter:
        print(*counter[max_idx], end=' ')
    max_idx -= 1



