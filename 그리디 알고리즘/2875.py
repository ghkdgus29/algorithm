girl, boy, intern = map(int, input().split())
team = 0
rest = 0

if girl >= 2 * boy:
    rest = girl - 2 * boy
    team = boy
else:
    rest = boy - girl // 2 + girl % 2
    team = girl // 2

if rest < intern:
    team = (team * 3 - (intern - rest)) // 3

print(team)
