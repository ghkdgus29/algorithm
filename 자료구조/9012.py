t = int(input())

for _ in range(t):
    s = input()
    vps_flag = True
    stack = []                      # 스택 사용

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:               # '(' 보다 ')' 가 많으면
                vps_flag = False        # vps 아님
                break
            stack.pop()

    if not stack and vps_flag:          # ')' 보다 '(' 가 많아
        print("YES")                    # 스택이 비어있으면 vps 아님
    else:
        print("NO")
