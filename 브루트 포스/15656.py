def fill(index, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(scope):
        ans[index] = numbers[i]
        fill(index + 1, scope, length)
        ans[index] = 0


scope, length = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

ans = [0] * length

fill(0, scope, length)
