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


n = int(input())
parent = [i for i in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    union(a, b)

ans = -1
root = find(1)
for p in parent:
    if root == find(p):
        ans += 1
print(ans)
