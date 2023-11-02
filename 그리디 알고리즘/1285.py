n = int(input())
coins = [list(input()) for _ in range(n)]

for y in range(n):                  # 뒤집기를 쉽게 하기 위해서 H -> 1, T -> 0 으로 변환
    for x in range(n):
        if coins[y][x] == 'T':
            coins[y][x] = 0
        else:
            coins[y][x] = 1

ans = n * n
for state in range(1 << n):         # 한 행을 뒤집은 경우 1, 한 행을 뒤집지 않은 경우를 0으로 하는 모든 경우의 수를 반복
    total = 0                # 모든 tail 개수

    for x in range(n):      # 한 열에 대해 tail 개수 검사
        tail_cnt = 0                # 한 열에 대한 tail 개수
        for y in range(n):
            cur = coins[y][x]
            if (state & (1 << y)) != 0:     # 만약 현재 위치의 동전이 뒤집은 행의 동전인 경우,
                cur = 1 - cur               # 동전을 뒤집는다.
            if cur == 0:                    # 만약 동전이 tail이라면
                tail_cnt += 1               # 한 열에 대한 tail 개수 증가
        total += min(tail_cnt, n - tail_cnt)    # 열을 뒤집지 않거나 (tail_cnt), 열을 뒤집어 (n - tail_cnt) 가장 적은 개수의 tail 개수를 만든다.

    ans = min(ans, total)           # 모든 경우의 수중 가장 작은 tail 개수가 정답

print(ans)
