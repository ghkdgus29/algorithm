dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
height, width = map(int, input().split())
a = [input() for _ in range(height)]  # 게임판
distance = [[0] * width for _ in range(height)]  # 거리 배열
visit = [[False] * width for _ in range(height)]  # 방문여부 체크


def go(x, y, cnt, color):
    if visit[y][x]:
        if cnt - distance[y][x] >= 4:           # 재방문 시, 거리가 4이면 cycle
            return True
        else:                                   # 거리가 4보다 작으면 cycle 아님
            return False

    visit[y][x] = True                  # 방문
    distance[y][x] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < width and 0 <= ny < height:
            if a[ny][nx] == color:
                if go(nx, ny, cnt + 1, color):      # 만약 cycle 형성 시, True 를 줄줄이 반환
                    return True
    return False                                    # cycle 형성이 안되면, False 를 줄줄이 반환


for y in range(height):
    for x in range(width):
        if not visit[y][x]:
            if go(x, y, 1, a[y][x]):                # cycle 이 형성되면 결과적으로 True 가 반환
                print('Yes')    
                exit()

print('No')
