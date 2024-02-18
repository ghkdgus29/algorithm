def pick(picks, idx):
    if idx >= n:
        if low_sum <= sum(picks) <= max_sum and max(picks) - min(picks) >= min_diff:
            global ans
            ans += 1
        return

    pick(picks + [problems[idx]], idx + 1)
    pick(picks, idx + 1)


n, low_sum, max_sum, min_diff = map(int, input().split())
problems = list(map(int, input().split()))
ans = 0

pick([], 0)
print(ans)

