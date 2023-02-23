def make_inequality_number(index, numbers: list):
    if len(numbers) != len(set(numbers)):  # 숫자 중복일 경우 바로 종료 (백트래킹)
        return

    if index == n + 1:
        ans.append(numbers)                 # 숫자 중복이 아닐 경우, ans 배열에 추가
        return

    if index == 0:                          # 첫 번째 인덱스는 아무 숫자나 상관없음
        for i in range(10):
            make_inequality_number(index + 1, numbers + [i])
    elif s[index - 1] == ">":
        for i in range(numbers[index - 1]):
            make_inequality_number(index + 1, numbers + [i])
    elif s[index - 1] == "<":
        for i in range(numbers[index - 1] + 1, 10):
            make_inequality_number(index + 1, numbers + [i])


n = int(input())
s = input().split()
ans = []

make_inequality_number(0, [])

print(''.join(map(str, ans[-1])))       # 배열 마지막 원소가 가장 큰 숫자
print(''.join(map(str, ans[0])))        # 배열 첫 번째 원소가 가장 작은 숫자
