class Node:
    order = 0                                   # 열 성분
    depth = 0                                   # 행 성분

    def __init__(self, left, right):
        self.left = left
        self.right = right


def inorder(idx, depth):
    if idx == -1:
        return

    inorder(nodes[idx].left, depth + 1)

    global order
    order += 1                              # 왼쪽부터 차례로 방문하기 때문에 방문 순서가 곧 x 성분이 된다.
    nodes[idx].order = order                # 현재 인덱스에 해당하는 노드를 방문하여 x 성분 입력
    nodes[idx].depth = depth                # 현재 인덱스에 해당하는 노드를 방문하여 y 성분 입력

    inorder(nodes[idx].right, depth + 1)


n = int(input())

order = 0
nodes = [None] * (n + 1)                    # 모든 노드를 저장하는 리스트
left = [10001] * (n + 1)                    # 해당 depth의 가장 왼쪽 성분의 x 좌표를 저장하는 리스트
right = [-1] * (n + 1)                      # 해당 depth의 가장 오른쪽 성분의 x 좌표를 저장하는 리스트
root_check = [False] + [True] * n           # root를 체크하기 위한 리스트, 문제에서 0번째 노드는 존재하지 않으므로 False 처리

for _ in range(n):                              # 노드를 생성하여 리스트에 저장
    p, c1, c2 = map(int, input().split())
    nodes[p] = Node(c1, c2)
    if c1 != -1:                                # 자식노드가 존재한다면, 자식노드들이 root가 아님을 체크
        root_check[c1] = False
    if c2 != -1:
        root_check[c2] = False

root = root_check.index(True)                   # root 노드 인덱스 찾기
inorder(root, 1)                            # root 노드를 시작으로 inorder traversal 시작

maxdepth = 0
for node in nodes:
    if node is None:                        # 0번째 노드는 존재하지 않으므로 None 일 경우 continue
        continue

    depth = node.depth
    order = node.order

    left[depth] = min(left[depth], order)           # 현재 depth의 가장 왼쪽에 위치하는 노드의 x 성분
    right[depth] = max(right[depth], order)         # 현재 depth의 가장 오른쪽에 위차하는 노드의 x 성분

    maxdepth = max(maxdepth, depth)                 # 주어진 트리의 최대 깊이 계산

ans = 0
ans_depth = 0

for i in range(1, maxdepth + 1):                # 주어진 트리의 모든 깊이에 대해 계산
    if ans < right[i] - left[i] + 1:
        ans = right[i] - left[i] + 1
        ans_depth = i

print(str(ans_depth) + " " + str(ans))
