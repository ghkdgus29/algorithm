def fill(index, prev_idx, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(prev_idx, scope):
        ans[index] = numbers[i]
        fill(index + 1, i, scope, length)
        ans[index] = 0


scope, length = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = [0] * length

fill(0, 0, scope, length)
