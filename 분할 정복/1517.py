def merge_sort_calculate(arr, start, end):
    if start == end:
        return 0

    mid = (start + end) // 2

    ans = merge_sort_calculate(arr, start, mid) + merge_sort_calculate(arr, mid + 1, end)

    tmp = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:                     # 값이 같은 경우에도 swap 이 일어나면 안되니까 <= 로 처리해주어야 한다.
            tmp.append(arr[left])
            left += 1
        else:
            ans += mid - left + 1
            tmp.append(arr[right])
            right += 1

    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= end:
        tmp.append(arr[right])
        right += 1

    for i in range(start, end + 1):
        arr[i] = tmp[i - start]

    return ans


n = int(input())
arr = list(map(int, input().split()))
print(merge_sort_calculate(arr, 0, n - 1))
