import collections

input()
cards = collections.Counter(list(map(int, input().split())))
input()

ans = []
for num in list(map(int, input().split())):
    if num in cards:
        ans.append(cards[num])
    else:
        ans.append(0)

print(*ans)
