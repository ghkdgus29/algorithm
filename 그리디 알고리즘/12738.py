def bin_search(nums: list, target: int):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid

    return start


n = int(input())
numbers = list(map(int, input().split()))
d = [numbers[0]]

for number in numbers[1:]:
    if d[-1] < number:
        d.append(number)
    else:
        d[bin_search(d, number)] = number

print(len(d))
