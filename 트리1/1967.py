import collections


class Edge:                                 # 간선 클래스
    def __init__(self, next, cost):
        self.next = next                      # 다음 노드 정보
        self.cost = cost                      # 현재 간선의 cost


n = int(input())

edges = [[] for _ in range(n + 1)]              # 해당 노드와 연결된 간선들을 저장하는 리스트
                                                # outer 리스트의 인덱스는 노드 번호를 나타내고,
                                                # 해당 인덱스에 저장된 inner 리스트는 노드와 연결된 간선들이다. (Edge 클래스)


def bfs(start):
    queue = collections.deque([start])
    dist[start] = 0

    while queue:
        node = queue.popleft()
        for edge in edges[node]:                            # 현재 노드와 연결된 간선들을 모두 조사
            if dist[edge.next] == -1:                           # 연결된 노드를 방문하지 않은 경우
                dist[edge.next] = dist[node] + edge.cost        # 거리값 계산해서 저장
                queue.append(edge.next)


for _ in range(n - 1):
    n1, n2, c = map(int, input().split())

    edges[n1].append(Edge(n2, c))
    edges[n2].append(Edge(n1, c))                   # 트리는 방향이 없는 그래프이므로, 두 노드를 모두 연결해야 한다.

dist = [-1] * (n + 1)
bfs(1)                                          # 임의의 노드에서 가장 먼 노드 구하기

start = 1
for i in range(2, n + 1):
    if dist[i] > dist[start]:                   # dist가 가장 큰 값의 인덱스가 가장 먼 노드가 된다.
        start = i

dist = [-1] * (n + 1)                           # start 노드에서 다시 최대거리를 구하기위해 dist 초기화
bfs(start)                                      # start 노드에서 가장 먼 노드거리 구하기
print(max(dist))
