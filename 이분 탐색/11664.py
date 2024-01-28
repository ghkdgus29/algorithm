def dist(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** (1 / 2)


x1, y1, z1, x2, y2, z2, x, y, z = map(int, input().split())
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1            # 기울기
left = 0.0
right = 1.0             # offset (0 ~ 1)

while left <= right:
    m1 = left + (right - left) / 3      # 삼분탐색의 1/3 지점
    m2 = right - (right - left) / 3     # 삼분탐색의 2/3 지점
    m1x = x1 + m1 * dx
    m1y = y1 + m1 * dy
    m1z = z1 + m1 * dz      # 기울기에 m1 offset 만큼 값을 곱해 좌표를 만듬
    m2x = x1 + m2 * dx
    m2y = y1 + m2 * dy
    m2z = z1 + m2 * dz      # 기울기에 m2 offset 만큼 값을 곱해 좌표를 만듬

    d1 = dist(m1x, m1y, m1z, x, y, z)
    d2 = dist(m2x, m2y, m2z, x, y, z)
    if d1 > d2:                             # m1 offset 을 곱해 구한 좌표보다, m2 offset 을 곱해 구한 좌표가 더 짧은 거리를 가짐
        left = m1 + 0.0000001
    else:                                   # m2 offset 을 곱해 구한 좌표보다, m1 offset 을 곱해 구한 좌표가 더 짧은 거리를 가짐
        right = m2 - 0.0000001

x0 = x1 + right * dx
y0 = y1 + right * dy
z0 = z1 + right * dz                    # 반복문을 탈출하고 나온 right 이 최소 거리가 되는 offset 을 가지고 있으므로,
                                        # 최소거리가 되는 점 x0, y0, z0 을 구한다.
ans = dist(x0, y0, z0, x, y, z)
print(round(ans, 6))
