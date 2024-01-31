def calculate(score):                   # 주어진 점수를 만족하는 구간이 몇 개가 나오는지 계산
    minimum = a[0]
    maximum = a[0]
    split_cnt = 1
    for i in range(1, len(a)):
        if minimum > a[i]:
            minimum = a[i]
        if maximum < a[i]:
            maximum = a[i]
        if maximum - minimum > score:           # 만약 현재 인덱스에서의 최대 - 최소 값이 점수를 넘으면
            split_cnt += 1                      # 현재 인덱스를 포함한 새로운 구간을 만든다.
            minimum = maximum = a[i]
    return split_cnt


n, m = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = max(a)
ans = -1
while left <= right:
    mid = (left + right) // 2       # 점수를 이분탐색으로 정한다.
    if calculate(mid) <= m:         # 해당 점수를 만족하는 그룹 개수가 주어진 그룹 개수보다 적은 경우
        right = mid - 1             # 점수를 줄여본다.
        ans = mid                   # 정답을 최소 점수값으로 갱신

    else:                           # 해당 점수를 만족하는 그룹 개수가 주어진 그룹 개수보다 많은 경우
        left = mid + 1              # 점수를 늘려본다.

print(ans)
