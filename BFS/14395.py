import collections
import sys

max_val = 10_0000_0000
given, target = map(int, input().split())

if given == target:         # 숫자가 같은 경우
    print(0)

visit = set()

queue = collections.deque()
queue.append((given, ''))
visit.add(given)

while queue:
    number, way = queue.popleft()

    if number == target:
        print(way)
        sys.exit()

    if number * number not in visit and number * number <= max_val:     # 곱하기 연산
        visit.add(number * number)
        queue.append((number * number, way + '*'))

    if number + number not in visit and number + number <= max_val:     # 더하기 연산
        visit.add(number + number)
        queue.append((number + number, way + '+'))

    if 1 not in visit:                                                  # 나누기 연산, 어떤수든지 1로 만든다.
        visit.add(1)
        queue.append((1, way + '/'))

print(-1)   # given 으로 target 을 만들 수 없는 경우
