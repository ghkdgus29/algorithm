import collections


def left_rotate(num):
    return (num % 1000) * 10 + num // 1000


def right_rotate(num):
    return (num % 10) * 1000 + num // 10


def print_result(target, given):
    ans = []
    while target != given:
        ans.append(how[target])
        target = via[target]

    print(''.join(ans[::-1]))


n = int(input())

for _ in range(n):
    visit = [False] * 10000
    via = [-1] * 10000                                      # 어디에서 왔는지 역추적하기 위한 리스트
    how = [''] * 10000                                      # 어떤 명령어로 이 숫자를 만들었는지 기록하는 리스트
    given, target = map(int, input().split())

    queue = collections.deque([given])
    visit[given] = True

    while queue:
        prev_num = queue.popleft()

        if prev_num == target:
            break

        if not visit[2 * prev_num % 10000]:
            visit[2 * prev_num % 10000] = True
            via[2 * prev_num % 10000] = prev_num
            how[2 * prev_num % 10000] = 'D'
            queue.append(2 * prev_num % 10000)

        if not visit[prev_num - 1 if prev_num - 1 >= 0 else 9999]:
            visit[prev_num - 1 if prev_num - 1 >= 0 else 9999] = True
            via[prev_num - 1 if prev_num - 1 >= 0 else 9999] = prev_num
            how[prev_num - 1 if prev_num - 1 >= 0 else 9999] = 'S'
            queue.append(prev_num - 1 if prev_num - 1 >= 0 else 9999)

        if not visit[left_rotate(prev_num)]:
            visit[left_rotate(prev_num)] = True
            via[left_rotate(prev_num)] = prev_num
            how[left_rotate(prev_num)] = 'L'
            queue.append(left_rotate(prev_num))

        if not visit[right_rotate(prev_num)]:
            visit[right_rotate(prev_num)] = True
            via[right_rotate(prev_num)] = prev_num
            how[right_rotate(prev_num)] = 'R'
            queue.append(right_rotate(prev_num))

    print_result(target, given)
