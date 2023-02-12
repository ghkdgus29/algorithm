def next_permutation(a: list):
    tail = len(a) - 1
    while tail > 0 and a[tail - 1] >= a[tail]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] >= a[change]:
        change -= 1

    a[tail - 1], a[change] = a[change], a[tail - 1]
    a[tail:] = reversed(a[tail:])
    return True


def get_max_value():
    total = 0
    for i in range(n - 1):
        total += abs(a[i] - a[i + 1])

    return total


n = int(input())
a = sorted(list(map(int, input().split())))

max_value = get_max_value()

while next_permutation(a):
    max_value = max(max_value, get_max_value())

print(max_value)