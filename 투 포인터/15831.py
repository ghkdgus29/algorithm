n, b, w = map(int, input().split())
s = input()
left = right = 0
counter = {'W': 0, 'B': 0}
ans = 0
while right <= n:
    if counter['B'] > b:
        counter[s[left]] -= 1
        left += 1
    else:
        if counter['W'] >= w:
            ans = max(ans, right - left)
        if right == n:
            break
        counter[s[right]] += 1
        right += 1

print(ans)
