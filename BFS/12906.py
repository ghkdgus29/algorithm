import collections

s = []                      # 현재 원판 위치 상태
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        s.append(temp[1])
    else:
        s.append('')

cnt = [0, 0, 0]             # A, B, C 원판 개수 세기
for i in range(3):
    for ch in s[i]:
        cnt[ord(ch) - ord('A')] += 1

d = {}
q = collections.deque()
q.append(tuple(s))
d[tuple(s)] = 0
while q:
    x = q.popleft()
    for i in range(3):          # from
        for j in range(3):      # to
            if i == j:              # 자기 자신으로 원판 옮기는 경우
                continue
            if len(x[i]) == 0:      # 옮길 원판이 없는 경우
                continue
            y = list(x[:])
            y[j] = y[j] + x[i][-1]  # from 의 마지막 원판을 to 의 끝부분으로 옮기기
            y[i] = y[i][:-1]        # from 의 마지막 원판을 제거하기
            y = tuple(y)
            if y not in d:          # 현재 형태가 없다면
                d[y] = d[x] + 1
                q.append(y)

ans = ['', '', '']
for i in range(3):                      # 정답의 하노이 탑 만들기
    for j in range(cnt[i]):
        ans[i] += chr(ord('A') + i)
print(d[tuple(ans)])                    # 정답 하노이 탑을 만드는데 필요한 횟수 출력
