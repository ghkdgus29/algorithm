MAX = 10000000


def split_team(index, first_team, second_team):
    if index == n:
        if not first_team:
            return MAX
        if not second_team:
            return MAX

        first_team_stat = 0
        for i in range(len(first_team)):
            for j in range(len(first_team)):
                if i == j:
                    continue
                first_team_stat += s[first_team[i]][first_team[j]]

        second_team_stat = 0
        for i in range(len(second_team)):
            for j in range(len(second_team)):
                if i == j:
                    continue
                second_team_stat += s[second_team[i]][second_team[j]]

        diff = abs(first_team_stat - second_team_stat)
        return diff

    ans = MAX
    ans = min(ans, split_team(index + 1, first_team + [index], second_team))
    ans = min(ans, split_team(index + 1, first_team, second_team + [index]))
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

print(split_team(0, [], []))
