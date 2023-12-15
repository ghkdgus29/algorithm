input()
have = set(list(map(int, input().split())))

input()
given = list(map(int,input().split()))

ans = []
for num in given:
    if num in have:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)
