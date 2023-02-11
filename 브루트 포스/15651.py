def fill(index, scope, length):             # 재귀를 이용한 문제 풀이 -> 시간 복잡도 O(N!)
    if index == length:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, scope + 1):
        ans[index] = i
        fill(index + 1, scope, length)
        ans[index] = 0


def fill2(index, selected, scope, length):  # 선택을 이용한 문제 풀이 -> 시간 복잡도 O(2^n)
    if selected == length:
        print(' '.join(map(str, ans)))
        return

    if index > scope:
        return

    ans[selected] = index                           # 선택하는 경우
    fill2(index+1, selected+1, scope, length)

    ans[selected] = 0                               # 선택하지 않는 경우
    fill2(index+1, selected, scope, length)


scope, length = map(int, input().split())
ans = [0] * length


# fill(0, scope, length)
fill2(1, 0, scope, length)