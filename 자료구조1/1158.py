total, interval = map(int, input().split())

given = [i for i in range(1, total+1)]
per = []
idx = 0

while given:
    count = interval
    given_len = len(given)

    while count > 1:                # interval 만큼 돌린다.
        count -= 1
        idx += 1
        idx %= given_len

    per.append(given.pop(idx))      # given 에서 빼서, per 에 넣는다.

print("<", end="")
print(*per, sep=', ', end="")
print(">")


