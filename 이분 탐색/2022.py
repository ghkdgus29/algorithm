def calculate(w):
    if min(x, y) < w:
        return 2
    return c * (1 / ((y ** 2 - w ** 2) ** (1 / 2)) + 1 / ((x ** 2 - w ** 2) ** (1 / 2)))


x, y, c = map(float, input().split())

left = 0
right = 3000000001

while left <= right:
    mid = (left + right) / 2
    calc = calculate(mid)
    if 1 > calc:
        left = mid + 0.0001
    else:
        right = mid - 0.0001

print(round(right, 3))
