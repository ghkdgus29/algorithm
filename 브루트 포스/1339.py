def prev_permutation(a: list):
    tail = len(a) - 1
    while tail > 0 and a[tail - 1] < a[tail]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] <= a[change]:
        change -= 1

    a[tail - 1], a[change] = a[change], a[tail - 1]
    a[tail:] = reversed(a[tail:])
    return True


def set_alpha_value():
    for idx, key in enumerate(alpha):
        alpha[key] = numbers[idx]


def calculate():
    sum = 0
    for word in words:
        value = 0
        for ch in word:
            value *= 10
            value += alpha[ch]
        sum += value

    return sum


n = int(input())
alpha = {}
numbers = []
words = []

val = 9
for _ in range(n):
    given = list(input())
    words.append(given)

    for ch in given:
        if ch in alpha:
            continue
        alpha[ch] = 0
        numbers.append(val)
        val -= 1

max_value = -1
set_alpha_value()

while True:
    max_value = max(max_value, calculate())
    if not prev_permutation(numbers):
        break

    set_alpha_value()

print(max_value)
