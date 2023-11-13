def bin_search(nums: list, target: int):    # target이 들어가야 하는 인덱스를 반환
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (end + start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid     # target 을 찾은 경우

    return start        # target 이 없는 경우


n = int(input())
numbers = list(map(int, input().split()))

d = []          # 가장 긴 부분 수열 개수를 구하기 위한 리스트

for num in numbers:
    index = bin_search(d, num)      # 숫자가 들어갈 인덱스를 찾는다.
    if index == len(d):                 # 만약 숫자가 리스트에서 가장 큰 값이면 인덱스는 리스트의 길이와 같다.
        d.append(num)                       # 이 경우, 리스트에 숫자를 추가한다.
    else:
        d[index] = num                  # 만약 숫자가 리스트에서 가장 큰 값이 아니면, 인덱스는 리스트 내부의 요소를 가리킨다.
                                            # 이 경우, 해당 인덱스의 요소를 숫자로 변경한다.

print(len(d))   # 리스트의 길이가 가장 긴 부분 수열 개수이다.
                # 리스트가 가장 긴 부분 수열을 의미하진 않는다.
