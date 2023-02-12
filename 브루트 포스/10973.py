def prev_permutation(a: list):
    tail = len(a) - 1
    while tail > 0 and a[tail] >= a[tail - 1]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] <= a[change]:
        change -= 1

    a[tail - 1], a[change] = a[change], a[tail - 1]

    a[tail:] = reversed(a[tail:])
    return True


n = int(input())
a = list(map(int, input().split()))

if prev_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
