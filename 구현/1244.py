# 남자 -> 배수의 스위치 변경
# 여자 -> 번호부터 최장길이 팰린드롬을 구한 뒤, 팰린드롬의 스위치 변경

# 남자 - 1, 여자 - 2

def multiply_change(start):
    for i in range(start, n, start + 1):
        a[i] = 1 - a[i]


def palindrome_change(left, right):
    if left < 0 or right >= n or a[left] != a[right]:
        return

    a[left] = 1 - a[left]
    if left != right:
        a[right] = 1 - a[right]

    palindrome_change(left - 1, right + 1)


n = int(input())
a = list(map(int, input().split()))

for _ in range(int(input())):
    gender, idx = map(int, input().split())
    idx -= 1
    if gender == 1:
        multiply_change(idx)
    else:
        palindrome_change(idx, idx)

for i in range(0, n, 20):
    for j in range(i, min(i + 20, n)):
        print(a[j], end=" ")
    print()
