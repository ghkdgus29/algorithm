def check(idx, start, num):
    if idx >= n:
        numbers[num] = True
        return

    for i in range(start, 4):
        check(idx + 1, i, num + offset[i])


offset = [1, 5, 10, 50]
n = int(input())
numbers = [False] * 1001

check(0, 0, 0)

print(sum(numbers))
