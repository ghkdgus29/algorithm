def prev_permutation(a: list):
    tail = len(a) - 1

    while tail > 0 and a[tail - 1] <= a[tail]:
        tail -= 1

    if tail == 0:
        return False

    change = len(a) - 1
    while a[tail - 1] <= a[change]:
        change -= 1
    a[tail - 1], a[change] = a[change], a[tail - 1]

    a[tail:] = reversed(a[tail:])
    return True


while True:
    given = list(map(int, input().split()))

    if given[0] == 0:
        break

    n = given[0]
    a = given[1:]

    d = [1] * 6 + [0] * (n - 6)     # [1,1,1,1,1,1,0 ....] 1인 인덱스는 로또번호로 선택, 0인 인덱스는 로또번호로 선택하지 않는다.

    while True:
        print(*[a[i] for i in range(n) if d[i] == 1])       # d[i] 가 1인 i번째 원소만 선택해 리스트를 만든다.

        if not prev_permutation(d):     # 1111110.. 수열로, 가장 큰 수열부터 시작하므로, 이전 수열을 찾는 함수를 만들어서 사용
            break
    print()