given = list(map(int, input().split()))

e, s, m = 1, 1, 1
year = 1

while e != given[0] or s != given[1] or m != given[2]:
    e += 1
    s += 1
    m += 1
    year += 1

    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

print(year)
