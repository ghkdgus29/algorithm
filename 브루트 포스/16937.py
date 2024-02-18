import itertools

w, h = map(int, input().split())
n = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

for sticker1, sticker2 in itertools.combinations(stickers, 2):
    s1w, s1h = sticker1
    s2w, s2h = sticker2

    for _ in range(2):
        for _ in range(2):
            if max(s1h, s2h) <= h and s1w + s2w <= w:   # 1번, 2번 스티커를 세로로 놓는 경우
                ans = max(ans, s1w * s1h + s2w * s2h)

            if max(s1w, s2w) <= w and s1h + s2h <= h:   # 1번, 2번 스티커를 가로로 놓는 경우
                ans = max(ans, s1w * s1h + s2w * s2h)

            s2w, s2h = s2h, s2w     # 2번 스티커 90도 회전
        s1w, s1h = s1h, s1w     # 1번 스티커 90도 회전

print(ans)
