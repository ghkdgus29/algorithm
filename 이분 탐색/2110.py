def count(dist):
    cnt = 1
    last = house[0]
    for each in house:
        if each - last >= dist:
            cnt += 1
            last = each

    return cnt


n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 1
right = 1000000000
ans = -1
while left <= right:
    mid = (left + right) // 2
    cnt = count(mid)
    if cnt < c:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)
