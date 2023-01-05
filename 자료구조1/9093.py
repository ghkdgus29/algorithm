t = int(input())
for _ in range(t):
    s = input()
    s_len = len(s)

    stk = []                            # 스택 사용

    for i in range(s_len):
        if s[i] != ' ':
            stk.append(s[i])
        else:
            while len(stk) > 0:
                print(stk.pop(), end='')
            print(" ", end='')          # 띄어쓰기

    while len(stk) > 0:                 # 마지막 단어 출력
        print(stk.pop(), end='')

    print()                             # 줄바꿈
