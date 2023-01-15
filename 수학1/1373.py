import collections

n = list(input())
octa = collections.deque([])

while n:
    multiplier = 1
    oct = 0

    for i in range(3):          # 2진수 3자리씩 끊어서 8진수로 계산
        if not n:
            break
        if n.pop() == "1":
            oct += multiplier
        multiplier *= 2

    octa.appendleft(oct)

print(''.join(map(str, octa)))
