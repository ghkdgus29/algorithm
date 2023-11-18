import re

formula = input()
splited = formula.split("-", 1)

ans = 0
for str_number in splited[0].split("+"):
    ans += int(str_number)

if len(splited) == 2:
    for str_number in re.split("[+-]", splited[1]):
        ans -= int(str_number)

print(ans)
