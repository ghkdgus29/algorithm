def calculate():
    val = numbers[0]

    for idx, op in enumerate(ops):
        if op == 0:
            val += numbers[idx + 1]
        elif op == 1:
            val -= numbers[idx + 1]
        elif op == 2:
            val *= numbers[idx + 1]
        else:
            if val < 0 < numbers[idx + 1]:
                val = -(-val // numbers[idx + 1])
            else:
                val //= numbers[idx + 1]

    global max_val, min_val
    max_val = max(max_val, val)
    min_val = min(min_val, val)


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


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())
ops = [0] * plus + [1] * minus + [2] * mult + [3] * div

global max_val, min_val
max_val = -1000000000
min_val = 1000000000

while True:
    calculate()

    if not next_permutation(ops):
        break

print(max_val)
print(min_val)
