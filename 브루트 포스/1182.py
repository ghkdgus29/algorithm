def find_sub(index):
    global ans
    if index == n:
        a = [series[x] for x in range(n) if selected[x] == 1]
        if a and sum(a) == target:
            ans += 1
        return

    selected[index] = 1             # index 번째를 선택한 경우
    find_sub(index + 1)

    selected[index] = 0             # index 번째를 선택하지 않은 경우
    find_sub(index + 1)


ans = 0

n, target = map(int, input().split())
selected = [0] * n
series = list(map(int, input().split()))

find_sub(0)
print(ans)
