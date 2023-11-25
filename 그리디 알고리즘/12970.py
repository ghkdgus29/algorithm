total_length, want = map(int, input().split())

for a in range(total_length + 1):       # A 개수 0 ~ 전체 길이 까지 반복
    b = total_length - a                # B 개수 = 전체 길이 - A 개수

    if a * b < want:                    # a * b 보다 원하는 순서쌍이 많은 경우는 불가능하다.
        continue

    cnt = [0] * (b + 1)                 # B 사이사이의 A 개수를 나타내는 배열
                                        # cnt[0] 은 뒤에 B가없는 맨 뒤의 A개수이고, cnt[b] 는 뒤에 B가 b개수 만큼 있는 맨 앞의 A개수를 의미한다.

    for i in range(a):                  # A를 B 사이사이에 집어넣는 반복
        x = min(b, want)                    # B개수와 필요한 순서쌍 개수의 최소값 위치에 집어넣는다.
        cnt[x] += 1                         # 해당 위치 A개수 증가
        want -= x                           # 필요한 순서쌍 개수 감소

    for i in range(b, -1, -1):          # B 사이사이의 A 개수를 나타내는 cnt 배열을 맨 뒤에서부터 반복
        for j in range(cnt[i]):             # 해당 위치의 A개수 만큼 'A' 출력
            print('A', end='')
        if i > 0:                           # 만약 현재 위치가 맨 뒤가 아니면 뒤이어 'B' 출력
            print('B', end='')
    print()
    exit()

print(-1)          # 주어진 길이로 만족할 수 없는 경우
