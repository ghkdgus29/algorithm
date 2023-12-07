import sys


def go(word: str, target: str):
    if len(word) < len(target):
        return
    if word == target:
        print(1)
        sys.exit()

    if word[0] == 'B':
        go(word[::-1][:-1][:], target)
    if word[-1] == 'A':
        go(word[:-1][:], target)


given = input()
target = input()

go(target, given)
print(0)
