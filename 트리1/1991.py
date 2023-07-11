n = int(input())

graph = {chr(ord('A') + i): [] for i in range(n)}

for _ in range(n):
    parent, child1, child2 = input().split()

    graph[parent].append(child1)
    graph[parent].append(child2)


def preorder(node):
    print(node, end='')
    if graph[node][0] != '.':
        preorder(graph[node][0])
    if graph[node][1] != '.':
        preorder(graph[node][1])


def inorder(node):
    if graph[node][0] != '.':
        inorder(graph[node][0])
    print(node, end='')
    if graph[node][1] != '.':
        inorder(graph[node][1])


def postorder(node):
    if graph[node][0] != '.':
        postorder(graph[node][0])
    if graph[node][1] != '.':
        postorder(graph[node][1])
    print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
