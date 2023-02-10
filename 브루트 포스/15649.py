def fill(index, scope, length):
    if index == length:                     # 수열의 모든 개수를 만족하면 출력 후 종료
        print(' '.join(map(str, ans)))
        return

    for i in range(1, scope + 1):           # 수열의 모든 개수를 만족하지 않으면, scope 만큼 반복
        if check[i]:                            # 숫자를 한번도 고르지 않은 경우
            ans[index] = i
            check[i] = False                    # 숫자를 정답에 추가하고, 골랐음을 체크
            fill(index + 1, scope, length)          # 인덱스를 증가시켜 재귀함수 호출
            ans[index] = 0
            check[i] = True                     # 재귀가 끝났으면, 다시 새로운 조합을 고르기 위해 초기화


scope, length = map(int, input().split())

check = [True] * (scope + 1)        # 골랐는지 체크하는 배열
ans = [0] * length                  # 고른 숫자들

fill(0, scope, length)
