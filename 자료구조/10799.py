given = list(input().replace("()", "*"))    # 레이저 치환

stack = []
bar_cnt = 0

for ch in given:
    if ch == "(":                   # 막대 시작부분을 만난 경우
        stack.append(ch)                # 스택에 push
    elif ch == "*":                 # 레이저를 만난 경우
        bar_cnt += len(stack)           # 막대 시작 부분 개수를 더한다
    elif ch == ")":                 # 막대 끝부분을 만난 경우
        stack.pop()                     # 스택에서 pop
        bar_cnt += 1                    # 막대 끝 부분 개수(+1) 를 더한다.

print(bar_cnt)
