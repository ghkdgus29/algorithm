n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

stack = []  # 뒷 사람이 앞 사람을 볼 수 없는 경우 스택에서 제거된다.
ans = 0
for h in a:
    current = [h, 1]
    while stack:
        if stack[-1][0] <= h:  # 뒷 사람이 앞 사람을 볼 수 없거나, 앞 사람과 키가 같은 경우
            prev_h, same_cnt = stack.pop()
            ans += same_cnt
            if prev_h == h:
                current[1] += same_cnt
        else:
            break

    if stack:
        ans += 1
    stack.append(current)

print(ans)
