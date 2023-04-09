import collections

node_cnt = int(input())
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(node_cnt - 1):                                   # 그래프 만들기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

given = list(map(int, input().split()))                         # 주어진 BFS 방문 순서

visit = [False] * (node_cnt + 1)                                # 노드 방문 여부 체크
parent = [-1] * (node_cnt + 1)                                  # 해당 노드의 부모 노드를 명시


def bfs(given: list):
    validation_offset = 1
    queue = collections.deque([1])
    visit[1] = True

    for _ in range(node_cnt):                       # 방문 순서의 개수만큼 for문 반복
        if not queue:                                           # 만약 모든 방문 순서를 검사하지 않았는데 큐가 비었다면
            return False                                        # False 반환

        current_node = queue.popleft()

        child_cnt = 0                                           # 현재 노드의 자식 개수
        for node in graph[current_node]:
            if not visit[node]:                                 # 현재 노드와 연결된 미방문 노드 -> 자식 노드
                parent[node] = current_node                     # 미방문 노드의 부모 노드 -> 현재 노드
                child_cnt += 1

        for child_offset in range(child_cnt):
            if parent[given[validation_offset + child_offset]] != current_node:         # 현재 검사하는 방문순서에서 자식 개수만큼 추가 검사를 진행
                return False                                                # 추가 검사 : 추가 검사를 한 노드들의 부모가 현재노드가 맞는 지 검사

            queue.append(given[validation_offset + child_offset])                       # 추가 검사를 통과한 노드들을 차례로 큐에 넣는다.
            visit[given[validation_offset + child_offset]] = True                       # 큐에 넣은 노드들을 방문처리

        validation_offset += child_cnt                                # 추가 검사를 시작할 부분인 검사 offset을 자식 개수만큼 증가
    return True                                    # for 문을 성공적으로 돌면 검사 종료, 올바른 방문 순서


print(1 if bfs(given) else 0)
