def calc(height):
    cnt = 0
    for tree in trees:
        cnt += max(tree - height, 0)
    return cnt


n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = 1000000000
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = calc(mid)
    if cnt >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
