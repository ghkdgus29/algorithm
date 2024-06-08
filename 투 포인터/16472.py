import collections

n = int(input())
s = input()
counter = collections.defaultdict(int)
left = right = 0
ans = -1

while right <= len(s):
    if len(counter) > n:
        counter[s[left]] -= 1
        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1
    else:
        ans = max(ans, right - left)  # right 포인터 = 추가할 문자
        if right == len(s):
            break
        counter[s[right]] += 1
        right += 1

print(ans)
