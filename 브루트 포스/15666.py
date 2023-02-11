def fill(index, prev_idx, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(prev_idx, scope):
        ans[index] = numbers[i]
        fill(index + 1, i, scope, length)
        ans[index] = 0


_, length = map(int, input().split())
numbers = sorted(set(map(int, input().split())))
scope = len(numbers)

ans = [0] * length

fill(0, 0, scope, length)
