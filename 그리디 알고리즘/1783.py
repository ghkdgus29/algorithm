h, w = map(int, input().split())

count = 0
if h >= 3:
    if w >= 7:
        count = 5
        count += w - 7
    else:
        count = min(4, w)

elif h == 2:
    count = min(4, (w - 1) // 2 + 1)
elif h == 1:
    count = 1

print(count)
