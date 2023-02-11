def fill(index, prev, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(prev, scope + 1):
        ans[index] = i
        fill(index + 1, i, scope, length)
        ans[index] = 0


scope, length = map(int, input().split())
ans = [0] * length

fill(0, 1, scope, length)
