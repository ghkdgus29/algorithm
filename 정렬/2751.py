def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    left = right = 0
    buf = []

    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            buf.append(left_arr[left])
            left += 1
        else:
            buf.append(right_arr[right])
            right += 1

    while left < len(left_arr):
        buf.append(left_arr[left])
        left += 1

    while right < len(right_arr):
        buf.append(right_arr[right])
        right += 1

    return buf


a = []
for _ in range(int(input())):
    a.append(int(input()))

ans = merge_sort(a)

for each in ans:
    print(each)
