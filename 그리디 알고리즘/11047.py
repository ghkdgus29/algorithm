n, target = map(int, input().split())
units = [int(input()) for _ in range(n)]

current_unit = units.pop()
count = 0
while target > 0:
    while current_unit > target:
        current_unit = units.pop()

    count += target // current_unit
    target = target % current_unit

print(count)
