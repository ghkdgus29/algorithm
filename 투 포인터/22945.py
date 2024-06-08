# 사이에 있는 사람 수 * min(picks)
n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1

score = -1
while left < right:
    score = max((right - left - 1) * min(a[left], a[right]), score)
    if a[left] < a[right]:
        left += 1
    else:
        right -= 1

print(score)
