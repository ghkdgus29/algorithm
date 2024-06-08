# 2번 나오는 부분 문자열 중 가장 긴 길이 찾기

def make_pi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


s = input()
ans = 0
for i in range(len(s) - 1):
    pi = make_pi(s[i:])
    ans = max(ans, max(pi))

print(ans)
