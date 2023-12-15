def move(start, end):
    print(start, end)


def hanoi_tower(n, start, end):     # 원판 개수, 시작 지점, 이동하고 싶은 지점
    if n == 1:                  # 원판이 한 개면 원하는 지점으로 이동시킨다.
        move(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end)    # n-1개의 원판을 원하는 지점이 아닌 다른 기둥으로 이동시킨다.
    move(start, end)                        # 맨 밑에 원판을 원하는 지점으로 이동시킨다.
    hanoi_tower(n-1, 6-start-end, end)      # n-1개의 원하는 지점이 아닌 다른 기둥에 있는 원판을 원하는 지점으로 이동시킨다.


n = int(input())
print(2**n - 1)
hanoi_tower(n, 1, 3)
