n, ascending, descending = map(int, input().split())

if ascending == 1 and descending == n:      # 오름차순 1개, 내림차순 n개인 경우
    print(*[i for i in range(n, 0, -1)])
    exit()

if descending == 1 and ascending == n:      # 내림차순 1개, 오름차순 n개인 경우
    print(*[i for i in range(1, n + 1)])
    exit()

number_generator = []               # 그룹의 시작숫자와 끝숫자를 튜플로 묶어 넣는다.
ans = []

if ascending + descending - 1 <= n <= ascending * descending:   # n이 해당 조건을 만족해야 정답을 만들 수 있다.
    number_generator.append((1, descending))                # 내림차순 개수를 만족하는 그룹 생성
    n -= descending

    group_size = n // (ascending - 1)                       # 나머지 그룹들의 기본 사이즈 설정
    one_plus_group_count = n % (ascending - 1)              # 나머지 그룹들중 한 개씩 더 가져가야 하는 그룹 개수

    for _ in range(one_plus_group_count):                   # 한 개씩 더 가져가야 하는 그룹만들기
        n -= group_size + 1
        prev_end_index = number_generator[-1][1]
        current_start_index = prev_end_index + 1
        number_generator.append((current_start_index, current_start_index + (group_size + 1) - 1))

    while n > 0:                                            # 기본 사이즈만큼만 가져가는 그룹만들기
        n -= group_size
        prev_end_index = number_generator[-1][1]
        current_start_index = prev_end_index + 1
        number_generator.append((current_start_index, current_start_index + group_size - 1))

    for start_index, end_index in number_generator:         # (시작 숫자, 끝 숫자) 를 바탕으로 그룹을 뒤집은 수열만들기
        for num in range(end_index, start_index - 1, -1):
            ans.append(num)

    print(*ans)

else:
    print(-1)
