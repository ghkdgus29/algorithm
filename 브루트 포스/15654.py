def fill(index, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(scope):
        if check[i]:
            check[i] = False
            ans[index] = numbers[i]
            fill(index + 1, scope, length)
            check[i] = True
            ans[index] = 0


scope, length = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

check = [True] * (scope + 1)
ans = [0] * length

fill(0, scope, length)