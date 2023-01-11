n = int(input())
given = list(input())
numbers = [int(input()) for _ in range(n)]
stack = []

for idx, ch in enumerate(given):
    if ch.isalpha():
        given[idx] = numbers[ord(ch) - ord('A')]    # 문자를 숫자로 변환

for ch in given:
    if type(ch) is not int:                     # 연산자인 경우
        second_num = stack.pop()
        first_num = stack.pop()
        if ch == "+":
            stack.append(first_num + second_num)
        elif ch == "-":
            stack.append(first_num - second_num)
        elif ch == "*":
            stack.append(first_num * second_num)
        elif ch == "/":
            stack.append(first_num / second_num)

    else:                                       # 피연산자인 경우
        stack.append(ch)

print('{:.2f}'.format(stack.pop()))