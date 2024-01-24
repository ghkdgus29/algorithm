def count(size):
    cnt = 0
    for each in a:
        cnt += each // size
    return cnt


k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]
left = 1
right = 2 ** 31 - 1
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = count(mid)
    if cnt >= n:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
