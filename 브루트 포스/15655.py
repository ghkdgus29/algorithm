def fill(index, selected, scope, length):
    if selected == length:
        print(' '.join(map(str, ans)))
        return

    if index >= scope:
        return

    ans[selected] = numbers[index]
    fill(index + 1, selected + 1, scope, length)

    ans[selected] = 0
    fill(index + 1, selected, scope, length)


scope, length = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

ans = [0] * length

fill(0, 0, scope, length)
