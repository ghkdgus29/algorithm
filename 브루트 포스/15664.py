def fill(index, prev_idx, scope, length):
    if index == length:
        answers.add(tuple(ans))
        return

    for i in range(prev_idx, scope):
        if check[i]:
            check[i] = False
            ans[index] = numbers[i]
            fill(index + 1, i, scope, length)
            check[i] = True
            ans[index] = 0


scope, length = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

check = [True] * (scope + 1)
ans = [0] * length
answers = set([])

fill(0, 0, scope, length)

for ans in sorted(list(answers)):
    print(' '.join(map(str, ans)))
