# 주어진 길이 L 를 가진 올바른 괄호 문자열의 개수

# i는 첫 번째 '(' 글자와 대응하는 ')' 의 인덱스
# D[L] = sum(D[i-2] * D[L-i]),  (i는 짝수, 2<=i<=L)

for _ in range(int(input())):
    L = int(input())
    d = [0] * (L + 3)

    d[0] = 1

    for l in range(2, L + 1, 2):
        tmp = 0
        for i in range(2, l + 1, 2):
            tmp += d[i - 2] * d[l - i]
        d[l] = tmp % 1000000007
    print(d[L])
