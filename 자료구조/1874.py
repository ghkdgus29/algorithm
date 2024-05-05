n = int(input())
stack = []                      # 숫자 스택
ans = []                        # +, - 스택
flag = True                     # 스택 수열 만족 여부
numbers = [int(input()) for _ in range(n)]  # 수열 입력

idx = 1

for number in numbers:          # 모든 입력 수열에 대해

    if not stack:               # 스택이 비어있다면 push
        stack.append(idx)
        idx += 1
        ans.append("+")

    while number != stack[-1] and idx <= n:     # 수열입력값과 스택의 top이 같거나
        stack.append(idx)                       # 입력 정수 범위를 초과하면 탈출
        idx += 1
        ans.append("+")

    if stack.pop() == number:       # 수열입력값과 스택에서 꺼낸값이 같은 경우
        ans.append("-")
    else:                           # 수열입력값과 스택에서 꺼낸값이 다른 경우
        flag = False                # 입력 정수 범위를 초과한 경우
        break

if flag:                        # 스택 수열인 경우
    for op in ans:
        print(op)

else:                           # 스택 수열이 아닌 경우
    print("NO")
