def next_permutation(a: list):
    tail = len(a) - 1
    while tail > 0 and a[tail] <= a[tail - 1]:       # 내림차순 검사 (가장 마지막 부분 수열을 찾는 동작)
        tail -= 1

    if tail == 0:                                   # 전부 내림차순이면 가장 마지막 수열임
        return False

    change = len(a) - 1
    while a[tail - 1] >= a[change]:                 # 다음 부분순열의 숫자와 교환
        change -= 1
    a[tail - 1], a[change] = a[change], a[tail - 1]

    a[tail:] = sorted(a[tail:])                     # 다음 부분순열을 오름차순으로 정렬 (가장 첫번째 부분 수열로 만듬)
    return True


n = int(input())
a = list(map(int, input().split()))

if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
