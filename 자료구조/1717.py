def union(a, b):
    p1 = find(a)
    p2 = find(b)
    parent[p2] = p1


def find(a):
    if parent[a] == a:
        return a
    else:
        p = find(parent[a])
        parent[a] = p
        return p


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
