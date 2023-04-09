node_cnt = int(input())
graph = [[] for _ in range(node_cnt + 1)]

for _ in range(node_cnt - 1):                           # 그래프 생성
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

given = list(map(int, input().split()))                 # 주어진 방문 순서
order = [0] * (node_cnt + 1)                            # 노드들의 우선 순위
visit = [False] * (node_cnt + 1)

for idx in range(node_cnt):                             # 주어진 방문 순서대로 노드들의 우선 순위를 설정
    order[given[idx]] = idx

for idx in range(1, node_cnt + 1):                      # 방문 순서 기반으로 인접 리스트를 정렬
    graph[idx].sort(key=lambda x: order[x])

result = []             # DFS 결과물


def dfs(current):                                       # 정렬된 인접 리스트에 대해 DFS 를 수행
    visit[current] = True                               # 만약 결과물이 주어진 방문 순서와 다르면 올바르지 않은 방문 순서 입력이다.
    result.append(current)

    for node in graph[current]:
        if not visit[node]:
            dfs(node)


dfs(1)

print(1 if result == given else 0)
