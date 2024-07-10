time, n, k, y1, y2, x1, x2 = map(int, input().split())


def check_black(l, point):
    x, y = point  # 현재 탐색중인 좌표
    center = l // n  # 검정색 칸의 한 변의 길이, 이전 시간의 정사각형 한 변의 길이

    if l == 1:  # 정사각형 한 변의 길이가 1이면 무조건 흰 정사각형
        return 0
    if center * (n - k) // 2 <= x < center * (n + k) // 2 and center * (n - k) // 2 <= y < center * (n + k) // 2:  # 가운데 검정색 칸 부분
        return 1

    x %= center
    y %= center  # 좌표를 이전 시간의 정사각형에서의 상대좌표로 변경
    return check_black(center, [x, y])


l = n ** time
for i in range(y1, y2 + 1):
    for j in range(x1, x2 + 1):
        print(check_black(l, [j, i]), end="")
    print()
