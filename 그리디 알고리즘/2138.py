n = int(input())
given = list(map(int, list(input())))
target = list(map(int, list(input())))

count = 0


def change(x, arr):
    if x == n - 2:
        arr[x] = 1 ^ arr[x]
        arr[x + 1] = 1 ^ arr[x + 1]
        return

    arr[x] = 1 ^ arr[x]
    arr[x + 1] = 1 ^ arr[x + 1]
    arr[x + 2] = 1 ^ arr[x + 2]


given_copy_1 = given[:]
count1 = 0

given_copy_2 = given
given_copy_2[0] = 1 ^ given_copy_2[0]
given_copy_2[1] = 1 ^ given_copy_2[1]
count2 = 1

for i in range(n - 1):
    if given_copy_1[i] != target[i]:
        count1 += 1
        change(i, given_copy_1)

    if given_copy_2[i] != target[i]:
        count2 += 1
        change(i, given_copy_2)

for i in range(n):
    if given_copy_1[i] != target[i]:
        count1 = 1000_0000
    if given_copy_2[i] != target[i]:
        count2 += 1000_0000

print(min(count1, count2) if min(count1, count2) != 1000_0000 else -1)
