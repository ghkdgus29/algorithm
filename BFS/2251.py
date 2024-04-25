# A는 비어있을때, C 의 가능한 물 용량
import collections

# 1 : C -> B
# 2 : C -> A
# 8 : C (2) -> A (8), C (0) -> B (2), A(0) -> C(8)
# 9 : C (1) -> B (9), C (0) -> A (1), B(0) -> C(9)
# 10: C,

# 경우의 수 3P2 = 6
# A -> B, C
# B -> A, C
# C -> A, B


moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
ans = [False] * 201
check = [[False] * 201 for _ in range(201)]
cap = list(map(int, input().split()))
sum = cap[2]

queue = collections.deque()
queue.append((0, 0))
check[0][0] = True
ans[cap[2]] = True

while queue:
    now = queue.popleft()
    cur = [now[0], now[1], sum - now[0] - now[1]]
    for f, t in moves:
        next = cur[:]
        next[t] += next[f]
        next[f] = 0
        if next[t] >= cap[t]:   # 물이 넘치는 경우
            next[f] = next[t] - cap[t]
            next[t] = cap[t]

        if not check[next[0]][next[1]]:
            check[next[0]][next[1]] = True
            queue.append((next[0], next[1]))
            if next[0] == 0:            # A 물통이 비어있는 경우
                ans[next[2]] = True

for i in range(0, cap[2] + 1):
    if ans[i]:
        print(i, end=' ')
print()
