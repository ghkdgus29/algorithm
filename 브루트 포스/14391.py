def calculate():
    total = 0
    for y in range(h):              # 가로합 계산
        subtotal = 0
        for x in range(w):
            if sign_matrix[y * w + x] == 0:     # 가로인 경우 -> 부분합 누적
                subtotal = subtotal * 10 + matrix[y][x]

            else:                               # 세로인 경우 -> 최종합에 부분합을 더함
                total += subtotal
                subtotal = 0

        total += subtotal

    for x in range(w):              # 세로합 계산
        subtotal = 0
        for y in range(h):
            if sign_matrix[y * w + x] == 0:     # 가로인 경우 -> 최종합에 부분합을 더함
                total += subtotal
                subtotal = 0

            else:                               # 세로인 경우 -> 부분합 누적
                subtotal = subtotal * 10 + matrix[y][x]
        total += subtotal

    return total


def find(index):
    global ans
    if index == h * w:
        ans = max(ans, calculate())             # matrix 값 계산 후 최대값을 ans로
        return

    sign_matrix[index] = 0              # 0 -> 가로체크
    find(index + 1)

    sign_matrix[index] = 1              # 1 -> 세로체크
    find(index + 1)


ans = 0
h, w = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(h)]
sign_matrix = [0] * (h * w)                             # 가로, 세로 체크용

find(0)
print(ans)
