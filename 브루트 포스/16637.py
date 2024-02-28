import collections


def work_out(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2


def calculate(picks):
    for i in range(len(picks) - 1):  # 괄호 안의 연산자가 2개 이상인 경우 validate
        if picks[i + 1] - picks[i] == 1:
            return

    tmp_number = collections.deque(number[:])
    tmp_op = collections.deque(operator[:])

    for pick_idx in picks[::-1]:  # 괄호 먼저 pre-calculate
        result = work_out(operator[pick_idx], number[pick_idx], number[pick_idx + 1])
        tmp_number[pick_idx] = result
        del tmp_number[pick_idx + 1]
        del tmp_op[pick_idx]

    while tmp_op:  # calculate
        op = tmp_op.popleft()
        num1 = tmp_number.popleft()
        num2 = tmp_number.popleft()
        tmp_number.appendleft(work_out(op, num1, num2))

    global ans
    ans = max(ans, tmp_number.pop())
    return


def pick(idx, picks):
    if idx >= len(operator):
        calculate(picks)
        return

    pick(idx + 1, picks + [idx])
    pick(idx + 1, picks)


n = int(input())
formula = input()
number = []
operator = []
ans = - float('inf')
for ch in formula:
    if ch in ['-', '+', '*']:
        operator.append(ch)
    else:
        number.append(int(ch))

pick(0, [])
print(ans)
