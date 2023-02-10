t = int(input())

for _ in range(t):
    maximum_m, maximum_n, wanted_m, wanted_n = map(int, input().split())

    wanted_m -= 1
    wanted_n -= 1           # 나머지 계산을 위해 1을 빼줌
    year = wanted_m         # m 을 고정

    cycled = True
    while year < maximum_m * maximum_n:     # n 만 바꿔가며 탐색, m*n은 공배수로 무조건 <1,1> 로 돌아온다.
        if year % maximum_n == wanted_n:
            print(year + 1)         # 나머지 계산을 위해 1을 빼줬으므로 1을 다시 더해줌
            cycled = False
            break
        year += maximum_m

    if cycled:
        print(-1)
