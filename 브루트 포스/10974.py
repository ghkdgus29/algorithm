def next_permutation(a: list):
    tail = len(a) - 1
    while tail > 0 and a[tail] <= a[tail - 1]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] >= a[change]:
        change -= 1

    a[tail - 1], a[change] = a[change], a[tail - 1]

    a[tail:] = reversed(a[tail:])
    return True


n = int(input())

a = [i for i in range(1, n + 1)]

print(' '.join(map(str, a)))
while next_permutation(a):
    print(' '.join(map(str, a)))
