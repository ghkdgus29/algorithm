# # 1 -1 1 1 -1 -1 -1 -1
# #
# # 1 0  1 2  1  0 -1 -2
import collections

formula = input()

a = []
for ch in formula:
    if ch == '(':
        a.append(1)
    else:
        a.append(-1)

s = [a[0]]
for i in range(1, len(a)):
    s.append(s[-1] + a[i])

s_rev = collections.deque([a[-1]])
for i in range(len(a) - 2, -1, -1):
    s_rev.appendleft(s_rev[0] + a[i])
cnt = 0
if s[-1] < 0:
    for i in range(len(s)):
        if formula[i] == ')':
            cnt += 1
        if s[i] == -1:
            break

elif s[-1] > 0:
    for i in range(len(s_rev) - 1, -1, -1):
        if formula[i] == '(':
            cnt += 1
        if s_rev[i] == 1:
            break

print(cnt)
