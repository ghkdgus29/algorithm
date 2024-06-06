import sys

# n = input()
# t = input()
#
# print(1 if t in n else 0)


###########################################
# KMP 알고리즘

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
    ans = []
    pi = makePi(p)
    j = 0
    for i in range(0, len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1

    return False


n = input()
t = input()

print(1 if kmp(n, t) else 0)
