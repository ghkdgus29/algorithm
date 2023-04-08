import sys
import collections

sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

check = [0] * n                     # 노드의 CYCLE 여부 & 방문 여부 체크

FOUND_CYCLE_NOT_INCLUDED = -2       # Cycle 의 재귀적 호출에 포함되었지만, Cycle에 포함되지는 않는 경우
NOT_FOUND_CYCLE = -1                # Cycle x
VISIT = 1                           # 해당 노드 방문
CYCLE = 2                           # 해당 노드를 방문했고, 해당 노드가 Cycle임


def check_cycle(current, prev):                                 # CYCLE을 찾는 함수 -> DFS 사용
    if check[current] == VISIT:  # 갔던 곳 재방문 -> cycle
        return current

    check[current] = VISIT                          # 현재 노드 방문

    for node in graph[current]:
        if node == prev:                            # 만약 이전에 방문한 노드이면 호출 종료
            continue
        res = check_cycle(node, current)            # 재귀적 호출의 반환값

        if res == FOUND_CYCLE_NOT_INCLUDED:         # 현재 재귀적 호출이 CYCLE 을 찾았지만, 호출한 노드는 CYCLE이 아닐 경우
            return FOUND_CYCLE_NOT_INCLUDED         # CYCLE 이 아님을 체크

        if res >= 0:                                # 현재 재귀적 호출이 CYCLE 인 경우,
            check[current] = CYCLE                  # 현재 노드를 CYCLE이라 체크
            if current == res:                              # 현재 노드가 CYCLE의 시작이면
                return FOUND_CYCLE_NOT_INCLUDED             # 이 호출메서드에게 더 이상 CYCLE이 아님을 반환
            else:
                return res                                  # 현재 노드가 CYCLE 안에 있으면, 이 호출메서드에게 CYCLE 임을 반환

    return NOT_FOUND_CYCLE                         # 재귀적 호출에서 CYCLE을 발견하지 못하면 CYCLE 이 아님을 반환


check_cycle(0, -1)

q = collections.deque()
distance = [-1] * n

for i in range(n):                                              # BFS를 통해 간선과 순환선 거리를 for 문
    if check[i] == CYCLE:                                   # 현재 노드가 순환선인 경우
        distance[i] = 0
        q.append(i)                                         # 모두 큐에 넣는다
    else:
        distance[i] = -1                                    # 노드가 순환선이 아닌 경우 방문하지 않았음을 의미하는 -1을 넣는다.

while q:
    current = q.popleft()
    for node in graph[current]:
        if distance[node] == -1:                            # 아직 방문하지 않은 노드라면
            q.append(node)                                  # 노드를 큐에 넣고
            distance[node] = distance[current] + 1          # 현재 노드의 거리에 1을 더해 해당 노드의 거리를 구한다.

print(*distance, sep=' ')
