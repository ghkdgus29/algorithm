given = list(input())
ans = []
op_stack = []
op_dict = {"*": 1, "/": 1, "+": 2, "-": 2, "(": 3}      # 연산자 우선 순위 (rank)

for ch in given:                # 차량기지 알고리즘을 사용
    if ch.isalpha():
        ans.append(ch)

    elif ch == "(":
        op_stack.append(ch)

    elif ch == ")":
        while op_stack[-1] != "(":
            ans.append(op_stack.pop())
        op_stack.pop()

    else:
        while op_stack and op_dict[op_stack[-1]] <= op_dict[ch]:
            ans.append(op_stack.pop())
        op_stack.append(ch)

while op_stack:
    ans.append(op_stack.pop())

print(''.join(ans))
