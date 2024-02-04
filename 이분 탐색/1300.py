n = int(input())
k = int(input())
left = 1
right = n*n
ans = -1
while left <= right:            # 이분 탐색으로 k 번째 숫자를 구한다
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n+1):         # 이분 탐색으로 구한 숫자를 row 인덱스 (1부터 시작) 로 나누면, 해당 숫자보다 작거나 같은 숫자 개수를 구할 수 있다.
        cnt += min(n, mid // i)
    if cnt >= k:                    # 작거나 같은 수가 k 보다 많은 경우
        ans = mid                       # 정답이 될 수 있다. (같은 크기가 여러개인 경우)
        right = mid - 1
    else:                           # 작거나 같은 수가 k 보다 작은 경우
        left = mid + 1

print(ans)
