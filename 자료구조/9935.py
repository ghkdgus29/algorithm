# 모든 폭발이 끝난 후 남는 문자열 출력
# 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

stack = []

word = input()
bomb = list(input())

for ch in word:
    stack.append(ch)
    if len(stack) >= len(bomb) and ch == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
