def fill(index, prev, scope, length):
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(prev + 1, scope + 1):
        if check[i]:
            check[i] = False
            ans[index] = i
            fill(index + 1, i, scope, length)
            check[i] = True
            ans[index] = 0


scope, length = map(int, input().split())

check = [True] * (scope + 1)
ans = [0] * length

fill(0, 0, scope, length)