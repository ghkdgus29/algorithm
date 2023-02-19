MAX = 10000000


def split_team(index, first_team, second_team):
    if index == n:                          # 팀원을 모두 나누면 종료조건 만족
        if len(first_team) != n // 2:
            return MAX
        if len(second_team) != n // 2:      # 만약 팀원이 반으로 나뉘지 않을 경우 MAX값 넣고 바로 종료
            return MAX

        first_team_stat = 0                 # 제대로 반으로 나뉜 경우, 팀 총 스탯 계산하기
        second_team_stat = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                first_team_stat += s[first_team[i]][first_team[j]]
                second_team_stat += s[second_team[i]][second_team[j]]

        return abs(first_team_stat - second_team_stat)

    if len(first_team) > n // 2:            # 만약 특정 팀이 인원수의 절반을 넘어가는 경우는
        return MAX                          # 잘못된 경우이므로 바로 MAX값 넣고 바로 죵료
    if len(second_team) > n // 2:
        return MAX

    ans = MAX
    ans = min(ans, split_team(index + 1, first_team + [index], second_team))    # index 번째 멤버를 첫 번째 팀에 넣는 경우
    ans = min(ans, split_team(index + 1, first_team, second_team + [index]))    # index 번째 멤버를 두 번째 팀에 넣는 경우
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

print(split_team(0, [], []))
