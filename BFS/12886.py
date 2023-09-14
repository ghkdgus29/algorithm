import collections

visit = [[False] * 1501 for _ in range(1501)]

x, y, z = map(int, input().split())
s = x + y + z                                   # [x, y] (합: x+y) -> [x+x, y-x] (합: x+y) , 따라서 두 수의 합이 변하지 않기 때문에 z = sum - x - y 로 표현하여 필요한 공간을 줄일 수 있다.


def bfs(x, y):                                  # 그래프를 만들어 만들 수 있는 돌 경우의 수 (x, y, s-x-y) 를 체크한다.
                                                # 만약 visit[x][y] = True 이면, 돌 [x개, y개, s-x-y (z개)] 를 만들 수 있다는 뜻이다.
    queue = collections.deque([(x, y)])
    visit[y][x] = True

    while queue:
        x, y = queue.popleft()

        rocks = [x, y, s - x - y]
        for i in range(3):
            for j in range(3):
                if rocks[i] < rocks[j]:                         # 만들 수 있는 모든 경우의 수를 체크
                    new_rocks = [x, y, s - x - y]
                    new_rocks[i] += rocks[i]                    # 작은돌 두배
                    new_rocks[j] -= rocks[i]                    # 큰돌 빼기
                    if not visit[new_rocks[0]][new_rocks[1]]:
                        visit[new_rocks[0]][new_rocks[1]] = True
                        queue.append((new_rocks[0], new_rocks[1]))


if s % 3 != 0:                      # 3으로 나눌 수 없다면, 절대로 균등하게 돌을 나눌 수 없다.
    print(0)

else:
    bfs(x, y)
    if visit[s // 3][s // 3]:               # 3으로 균등하게 나눈 곳을 방문하였다면
        print(1)
    else:
        print(0)
