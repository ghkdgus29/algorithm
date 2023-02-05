def possible(n):                    # 해당 번호로 숫자 버튼을 눌러 이동가능한지 확인
    for digit in list(str(n)):
        if digit in breakdown:
            return False

    return True


wanted = int(input())
if int(input()) == 0:
    breakdown = []
else:
    breakdown = list(input().split())

ans = wanted - 100
if ans < 0:
    ans = -ans

for i in range(1000000):        # 0 ~ 100만의 숫자에 대해 모두 검사
    if possible(i):
        digit_moved_and_pushed = len(str(i)) + abs(i - wanted)
        ans = min(ans, digit_moved_and_pushed)

print(ans)
