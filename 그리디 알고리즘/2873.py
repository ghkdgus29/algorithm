h, w = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(h)]

ans = ''

if h % 2 == 1:              # 높이가 홀수면, 모든 땅을 밟을 수 있다.
    for y in range(h):
        if y % 2 == 0:              # 오른쪽 끝까지 이동
            ans += 'R' * (w - 1)
            if y != h - 1:              # 만약 맨 아랫줄이 아니라면, 아래로 이동
                ans += 'D'
        else:                       # 왼쪽 끝까지 이동
            ans += 'L' * (w - 1)
            ans += 'D'

elif w % 2 == 1:            # 너비가 홀수면, 모든 땅을 밟을 수 있다.
    for x in range(w):
        if x % 2 == 0:
            ans += 'D' * (h - 1)    # 아래쪽 끝까지 이동
            if x != w - 1:
                ans += 'R'              # 만약 맨 오른쪽줄이 아니라면, 오른쪽으로 이동
        else:
            ans += 'U' * (h - 1)    # 위쪽 끝까지 이동
            ans += 'R'

else:
    x = 1
    y = 0
    for i in range(h):                      # 안 밟을 한 칸중 가장 기쁨이 작은 칸을 찾는다.
        for j in range(w):
            if (i + j) % 2 == 1:                # 체스판의 백색칸이 시작이라면, i+j 가 홀수인 칸은 흑색칸
                if land[y][x] > land[i][j]:
                    y, x = i, j

    x1 = 0
    y1 = 0
    x2 = w - 1
    y2 = h - 1
    behind = ''         # 끝 위치에서의 경로를 거꾸로 넣는 임시 저장소

    while y2 - y1 > 1:                  # 높이가 2줄이 될때까지 반복
        if y1 + 1 < y:                      # 시작 위치와 시작위치 바로 아래에 안 밟을 칸이 없다면 두 줄의 이동경로를 예상할 수 있다.
            ans += 'R' * (w - 1)
            ans += 'D'
            ans += 'L' * (w - 1)
            ans += 'D'
            y1 += 2                         # 시작 위치를 2칸 아래로 이동

        if y < y2 - 1:                      # 끝 위치와 끝위치 바로 위에 안 밟은 칸이 없다면 두 줄의 이동경로를 예상할 수 있다.
            behind += 'R' * (w - 1)             # 경로를 임시 저장소에 거꾸로 넣는다.
            behind += 'D'
            behind += 'L' * (w - 1)
            behind += 'D'
            y2 -= 2                         # 끝 위치를 2칸 위로 이동

    while x2 - x1 > 1:                  # 너비가 2줄이 될때까지 반복
        if x1 + 1 < x:                      # 시작 위치와 시작 위치 바로 오른쪽에 안 밟을 칸이 없다면, 두 줄의 이동경로를 예상할 수 있다.
            ans += 'DRUR'
            x1 += 2                         # 시작 위치를 2칸 오른쪽으로 이동

        if x < x2 - 1:                      # 끝 위치와 끝 위치 바로 왼쪽에 안 밟을 칸이 없다면, 두 줄의 이동경로를 예상할 수 있다.
            behind += 'DRUR'
            x2 -= 2                         # 끝 위치를 2칸 왼쪽으로 이동

    if y == y1:                         # 2x2 칸만 남아, 경로를 분기를 나눠 계산할 수 있다.
        ans += 'DR'
    else:
        ans += 'RD'

    ans += behind[::-1]                 # 끝 위치에서의 거꾸로 넣은 경로를 뒤집어 시작 위치에서의 경로와 합친다.

print(ans)
