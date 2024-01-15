from collections import namedtuple

Building = namedtuple('Building', ['left', 'height', 'right'])
Pair = namedtuple('Pair', ['x', 'height'])


def append(ans: [Pair], p: Pair):
    if ans:
        if ans[-1].height == p.height:                      # 이전 Pair 와 높이가 같은 경우, 스카이라인을 결정짓는 값이 아니므로 그냥 버린다.
            return
        if ans[-1].x == p.x:                                # 이전 Pair 와 x 좌표는 같지만, 높이가 더 높은 경우엔 해당 값을 갱신한다.
            ans[-1] = Pair(ans[-1].x, p.height)
            return
    ans += [p]                                              # 정답 리스트에 Pair 를 추가


def merge(a: [Building], start, end):           # 병합 정렬을 하면서 스카이라인을 결정
    if start == end:
        return [                                        # 스카이라인 배열이 더 이상 쪼갤 수 없는 하나 짜리 건물인 경우
            Pair(a[start].left, a[start].height),           # 시작 부분
            Pair(a[start].right, 0)                         # 끝 부분
        ]

    mid = (start + end) // 2
    l = merge(a, start, mid)
    r = merge(a, mid + 1, end)

    buf = []
    h1 = h2 = 0                                 # h1, h2 는 왼쪽 스카이라인, 오른쪽 스카이라인에서의 현재 건물 높이
    i = j = 0
    while i < len(l) and j < len(r):
        u = l[i]
        v = r[j]                                # u, v 는 왼쪽 스카이라인의 Pair, 오른쪽 스카이라인의 Pair 를 의미
        if u.x < v.x:                   # 왼쪽 건물의 x 좌표가 우선한 경우
            x = u.x
            h1 = u.height
            h = max(h1, h2)             # 왼쪽 건물 현재 높이와, 이전에 있던 오른쪽 건물 현재 높이 중 큰 것을 스카이라인 높이로 결정
            append(buf, Pair(x, h))
            i += 1
        else:                           # 오른쪽 건물의 x 좌표가 우선한 경우
            x = v.x
            h2 = v.height
            h = max(h1, h2)             # 오른쪽 건물 현재 높이와, 이전에 있던 왼쪽 건물 현재 높이 중 큰 것을 스카이라인 높이로 결정
            append(buf, Pair(x, h))
            j += 1

    while i < len(l):
        append(buf, l[i])
        i += 1

    while j < len(r):
        append(buf, r[j])
        j += 1

    return buf


n = int(input())
a = [Building(*map(int, input().split())) for _ in range(n)]
a.sort()
ans = merge(a, 0, n - 1)
for x, height in ans:
    print(x, height, end=' ')
print()
