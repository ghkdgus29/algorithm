# 계란 - 내구도, 무게
# 충돌 시, 상대 계란의 무게만큼 내구도가 깎인다.
# 내구도가 0이하가 되면 계란은 깨진다.

# 최대한 많은 계란을 깨야 한다.
# 가장 왼쪽 계란을 들고, 다른 하나랑 박치기 후 제자리에 놓는다.
# 더 이상 칠 계란이 없으면 종료
# 이후 다음칸 계란을 들고 다시 박치기
# 만약 가장 오른쪽에 계란을 든 경우 과정 종료

# 계란 개수
# 내구도, 무게
# 내구도, 무게
# 내구도, 무게 ...

# 깰 수 있는 계란의 최대 개수 출력

n = int(input())
eggs = []
ans = 0
for _ in range(n):
    durability, weight = map(int, input().split())
    eggs.append([durability, weight])


def pick_and_go(idx, egg_state):
    if idx >= n:
        cnt = 0
        for d, _ in egg_state:
            if d <= 0:
                cnt += 1
        global ans
        ans = max(ans, cnt)
        return

    hold_durability, hold_weight = egg_state[idx]
    if hold_durability <= 0:
        pick_and_go(idx + 1, egg_state)
        return

    hit = False
    for i in range(n):
        if i == idx:
            continue

        next_durability, next_weight = egg_state[i]
        if next_durability <= 0:
            continue

        egg_state[idx][0] -= next_weight
        egg_state[i][0] -= hold_weight

        hit = True
        pick_and_go(idx + 1, egg_state)

        egg_state[idx][0] += next_weight  # roll back
        egg_state[i][0] += hold_weight

    if not hit:
        pick_and_go(idx + 1, egg_state)


pick_and_go(0, eggs)

print(ans)

