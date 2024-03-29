n, m = map(int, input().split())
worst_combi = set()

for _ in range(m):
    buf = list(map(int, input().split()))

    for i in range(1, n + 1):
        if i in buf:
            continue
        worst_combi.add(tuple(sorted(buf + [i])))

print(n * (n - 1) * (n - 2) // (3 * 2) - len(worst_combi))
