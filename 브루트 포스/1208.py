n, target = map(int, input().split())
m = n // 2  # 3 4    -> 2
n -= m  # 0 1 2 -> 3

a = list(map(int, input().split()))


def make_sub_sum(start, end):
    size = end - start
    result = []

    def pick(idx, sum):
        if idx >= size:
            result.append(sum)
            return

        pick(idx + 1, sum)
        pick(idx + 1, sum + a[start + idx])

    pick(0, 0)
    return sorted(result)


pre = make_sub_sum(0, n)
post = make_sub_sum(n, n + m)

ans = 0
left = 0
right = len(post) - 1

while left < len(pre) and right >= 0:
    if pre[left] + post[right] == target:
        cur = pre[left]
        left_cnt = 0
        while left < len(pre) and pre[left] == cur: # 왼쪽 같은거 찾기
            left += 1
            left_cnt += 1

        cur = post[right]
        right_cnt = 0
        while right >= 0 and post[right] == cur:    # 오른쪽 같은거 찾기
            right -= 1
            right_cnt += 1
        ans += left_cnt * right_cnt

    elif pre[left] + post[right] > target:
        right -= 1

    else:
        left += 1

if target == 0:
    ans -= 1
print(ans)
