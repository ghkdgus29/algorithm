def find(index, summ):
    if index >= n:
        check[summ] = True
        return

    find(index + 1, summ + numbers[index])
    find(index + 1, summ)


check = [False] * (100000 * 20 + 1)
n = int(input())
numbers = list(map(int, input().split()))

find(0, 0)

print(check.index(False))
