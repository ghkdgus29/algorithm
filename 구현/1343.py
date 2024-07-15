import re
import sys

s = input()
x_nums = [len(i) for i in re.sub(r'\.+', '.', s.strip('.')).split('.')]
dot_nums = [len(i) for i in re.sub(r'X+', 'X', s.strip('X')).split('X')]

if len(x_nums) == 1 and x_nums[0] == 0:
    x_nums.pop()

if len(dot_nums) == 1 and dot_nums[0] == 0:
    dot_nums.pop()

poly = []
for num in x_nums:
    aaaa = 0
    while num >= 4:
        num -= 4
        aaaa += 1

    bb = 0
    if num == 2:
        bb += 1
        num -= 2

    if num > 0:
        aaaa = 0
        bb = 0

    poly.append((aaaa, bb))

ans = ""
if s[0] == 'X':  # X 시작 시, X 부분이 .부분보다 1개 더 많거나 같다.
    for i in range(len(dot_nums)):
        aaaa, bb = poly[i]
        if aaaa == 0 and bb == 0:
            print(-1)
            sys.exit(0)

        ans += aaaa * 'AAAA'
        ans += bb * 'BB'
        ans += dot_nums[i] * '.'

    if len(x_nums) > len(dot_nums):
        aaaa, bb = poly[-1]
        if aaaa == 0 and bb == 0:
            print(-1)
            sys.exit(0)

        ans += aaaa * 'AAAA'
        ans += bb * 'BB'

else:
    for i in range(len(x_nums)):
        ans += dot_nums[i] * '.'

        aaaa, bb = poly[i]
        if aaaa == 0 and bb == 0:
            print(-1)
            sys.exit(0)
        ans += aaaa * 'AAAA'
        ans += bb * 'BB'

    if len(x_nums) < len(dot_nums):
        ans += dot_nums[-1] * '.'

print(ans)
