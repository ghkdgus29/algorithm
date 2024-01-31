def count(size):
    if size < max_lecture_size:
        return 10000000000

    cnt = 1
    current_size = 0
    for each in lectures:
        if current_size + each > size:
            cnt += 1
            current_size = 0

        current_size += each
    return cnt


_, m = map(int, input().split())

lectures = list(map(int, input().split()))
max_lecture_size = max(lectures)
left = 1
right = 10000000000
ans = -1
while left <= right:
    mid = (left + right) // 2
    blue_lay_cnt = count(mid)

    if blue_lay_cnt > m:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)

# 1 1
# 100

# 5 1
# 1000 1000 1000 1000 1000

# 9 4
# 1 2 3 4 5 6 7 8 9

# 9 3
# 9 8 7 6 5 4 3 2 1

# 2 2
# 1000 3

# 9 3
# 1 1 1 1 1 1 1 1 5
