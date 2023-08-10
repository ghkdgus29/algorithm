def calculate(index, plus, minus, mult, div, result):
    if index >= n - 1:
        global max_val, min_val
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    value = numbers[index + 1]

    if plus > 0:
        calculate(index + 1, plus - 1, minus, mult, div, result + value)

    if minus > 0:
        calculate(index + 1, plus, minus - 1, mult, div, result - value)

    if mult > 0:
        calculate(index + 1, plus, minus, mult - 1, div, result * value)

    if div > 0:
        if result < 0:
            calculate(index + 1, plus, minus, mult, div - 1, -(-result // value))

        else:
            calculate(index + 1, plus, minus, mult, div - 1, result // value)


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())

max_val, min_val = -1000000001, 1000000001

calculate(0, plus, minus, mult, div, numbers[0])

print(max_val)
print(min_val)
