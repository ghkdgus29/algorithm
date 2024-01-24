import sys


def calc(n):
    count = 0
    start = 1
    length = 1
    while start <= n:
        end = start * 10 - 1        # 9, 99, 999 와 같은 자릿수에서 마지막 수
        if end > n:                 # 구하는 숫자보다 마지막 수가 큰 경우, 구하는 숫자가 end 가 된다.
            end = n
        count += (end - start + 1) * length     # ex) 10 ~ 99 -> (99 - 10 + 1) * 2 개의 자릿수를 갖는다.
        start *= 10
        length += 1
    return count


n, k = map(int, input().split())
if calc(n) < k:
    print(-1)
    sys.exit(0)

left = 1
right = n
number = 0
while left <= right:         # 이분 탐색을 사용해 자리수 개수를 만족하는 숫자를 구한다.
    mid = (left + right) // 2
    length = calc(mid)
    if length < k:              # 자리수가 작으면 숫자 증가
        left = mid + 1
    else:                       # 자리수가 크거나 같으면 숫자 감소
        number = mid            # 자리수가 크거나 같은 경우엔 정답이 될 수 있으므로 ans = mid
        right = mid - 1

s = str(number)                 # 해당 숫자에서 정확한 k 번째 숫자를 구하기 위해 문자열로 변환
l = calc(number)                # 해당 숫자의 자리수
print(s[len(s) - (l - k) - 1])

print(calc(n))
