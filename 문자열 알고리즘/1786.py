def makePi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, p):
    pi = makePi(p)
    ans = []
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                ans.append(i - len(p) + 1 + 1)
                j = pi[j]
            else:
                j += 1
    return ans

s = input()
p = input()

ans = kmp(s, p)
print(len(ans))
for idx in ans:
    print(idx, end=" ")
