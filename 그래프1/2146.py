# import collections
#
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# group = [[0] * n for _ in range(n)]
# distance = [[0] * n for _ in range(n)]
# group_index = 0
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# for y in range(n):                                          # 섬 별로 그룹으로 묶어준다.
#     for x in range(n):
#         if graph[y][x] == 1 and group[y][x] == 0:
#             group_index += 1                                # 그룹 인덱스를 증가 시켜 섬끼리 구별
#             group[y][x] = group_index
#
#             queue = collections.deque()
#             queue.append((x, y))
#             while queue:
#                 current_x, current_y = queue.popleft()
#                 for i in range(4):
#                     nx = current_x + dx[i]
#                     ny = current_y + dy[i]
#                     if 0 <= nx < n and 0 <= ny < n:
#                         if graph[ny][nx] == 1 and group[ny][nx] == 0:  # group[ny][nx] 가 0이면 방문하지 않은 지역
#                             group[ny][nx] = group_index
#                             queue.append((nx, ny))
#
# min_distance = 1000000
#
# for group_idx in range(1, group_index+1):
#     queue = collections.deque()
#     for y in range(n):                              # 모든 맵을 탐색하며
#         for x in range(n):
#             distance[y][x] = -1                     # 현재 그룹 인덱스의 섬이 아닌 지역의 거리는 -1로 설정
#             if group[y][x] == group_idx:
#                 queue.append((x, y))                # 섬을 모두 큐에 넣는다.
#                 distance[y][x] = 0                  # 현재 그룹 인덱스의 섬인 부분은 거리를 0으로 설정
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:                     # BFS를 사용하여
#                 if distance[ny][nx] == -1:                      # 섬이 아닌, 미방문 지역의 거리 계산
#                     distance[ny][nx] = distance[y][x] + 1
#                     queue.append((nx, ny))
#
#     for y in range(n):
#         for x in range(n):                                      # 모든 맵을 탐색
#             if graph[y][x] == 1 and group[y][x] != group_idx:   # 만약 지금 위치가, 현재 그룹 인덱스의 섬이 아니면
#                 if min_distance > distance[y][x] - 1:           # 해당 위치까지의 다리길이를 측정하고, 최소를 비교
#                     min_distance = distance[y][x] - 1
#
# print(min_distance)

# 위의 방법은 섬 개수만큼 BFS를 수행하는 느린 로직이다.


# 아래의 방법은 섬을 확장하는 방식으로, BFS를 한번 수행하는 빠른 로직이다.

import collections

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
group = [[0] * n for _ in range(n)]
distance = [[0] * n for _ in range(n)]
group_index = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for y in range(n):                                          # 섬 별로 그룹으로 묶어준다.
    for x in range(n):
        if graph[y][x] == 1 and group[y][x] == 0:
            group_index += 1                                # 그룹 인덱스를 증가 시켜 섬끼리 구별
            group[y][x] = group_index

            queue = collections.deque()
            queue.append((x, y))
            while queue:
                current_x, current_y = queue.popleft()
                for i in range(4):
                    nx = current_x + dx[i]
                    ny = current_y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] == 1 and group[ny][nx] == 0:  # group[ny][nx] 가 0이면 방문하지 않은 지역
                            group[ny][nx] = group_index
                            queue.append((nx, ny))


                                # for문 제거 -> 섬 개수만큼 반복하지 않는다.
queue = collections.deque()
for y in range(n):
    for x in range(n):
        distance[y][x] = -1             # 섬이 아닌 지역의 거리는 -1로 설정
        if graph[y][x] == 1:
            queue.append((x, y))        # 섬은 모두 큐에 넣고 거리는 0으로 설정
            distance[y][x] = 0

while queue:                                            # BFS 를 사용하여, 섬이 아닌 지역의 거리계산 및 섬 확장
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if distance[ny][nx] == -1:                          # 미방문 지역일 경우
                distance[ny][nx] = distance[y][x] + 1           # 거리 계산
                group[ny][nx] = group[y][x]                     # 연결된 섬의 그룹 인덱스를 넣어준다 -> 섬 확장
                queue.append((nx, ny))

min_distance = 1000000
for y in range(n):
    for x in range(n):                                          # 모든 맵을 탐색
        for i in range(4):
            neighbor_x = x + dx[i]
            neighbor_y = y + dy[i]
            if 0 <= neighbor_x < n and 0 <= neighbor_y < n:
                if group[y][x] != group[neighbor_y][neighbor_x]:            # 만약 인접한 지역이 다른 섬일 경우 다리를 놓을 수 있다.
                    if min_distance > distance[y][x] + distance[neighbor_y][neighbor_x]:          # 다리의 최소길이를 계산
                        min_distance = distance[y][x] + distance[neighbor_y][neighbor_x]

print(min_distance)

