# 모든 문자가 연속해서 그룹화된 단어 개수 구하기

ans = 0
for _ in range(int(input())):
    checker = set()
    word = input()
    current = " "
    group_word = True
    for ch in word:
        if ch != current:
            if ch in checker:
                group_word = False
            checker.add(ch)
            current = ch
    if group_word:
        ans += 1

print(ans)

