n, m = map(int, input().split())
unheard = set()
ans = []

for _ in range(n):
    unheard.add(input())

for _ in range(m):
    unseen = input()
    if unseen in unheard:
        ans.append(unseen)

print(len(ans))
for name in sorted(ans):
    print(name)
