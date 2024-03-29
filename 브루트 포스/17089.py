node_cnt, edge_cnt = map(int, input().split())

graph = [set() for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    n1, n2 = map(int, input().split())
    graph[n1].add(n2)
    graph[n2].add(n1)

ans = float('inf')
for i in range(1, node_cnt + 1 - 2):
    for j in range(i + 1, node_cnt + 1 - 1):
        if j in graph[i]:       # 고른 두 노드가 서로 친구일때만 실행
            for k in range(j + 1, node_cnt + 1):
                if k in graph[i] and k in graph[j]:
                    ans = min(ans, len(graph[i]) + len(graph[j]) + len(graph[k]) - 6)

print(ans if ans != float('inf') else -1)

# 총 시간 복잡도는 O(n^3) 이 아니라, O(n^2 + m*n)
# n 은 사람 수, m 은 만들 수 있는 친구쌍의 수
