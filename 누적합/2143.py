import collections

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

s_a = [0]
for val in a:
    s_a.append(s_a[-1] + val)
s_b = [0]
for val in b:
    s_b.append(s_b[-1] + val)

a_counter = collections.defaultdict(int)
b_counter = collections.defaultdict(int)

for i in range(n + 1):
    for j in range(0, i):
        a_counter[s_a[i] - s_a[j]] += 1

for i in range(m + 1):
    for j in range(0, i):
        b_counter[s_b[i] - s_b[j]] += 1

ans = 0
for a_sum in a_counter.keys():
    if target - a_sum in b_counter.keys():
        ans += b_counter[target - a_sum] * a_counter[a_sum]

print(ans)
