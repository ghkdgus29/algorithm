# 단축키 지정이 안되었다면 단어의 첫 글자를 단축키로 지정
# 단어는 오른쪽으로 이동
# 모든 단어의 첫 글자가 지정이 되었다면 차례대로 알파벳 이동하며 단축키 지정
# 어떤것도 지정할 수 없다면 그냥 놔둠
# 대소문자 구분 x

shortcut = set()

for _ in range(int(input())):
    given = input()

    shortcut_idx = -1

    idx = -1
    for word in given.split():
        if shortcut_idx == -1 and word[0].lower() not in shortcut:
            shortcut_idx = idx + 1
            shortcut.add(word[0].lower())
        else:
            idx += len(word) + 1

    if shortcut_idx == -1:
        for idx, ch in enumerate(given):
            if shortcut_idx == -1 and ch != " " and ch.lower() not in shortcut:
                shortcut_idx = idx
                shortcut.add(ch.lower())

    for idx, ch in enumerate(given):
        if idx == shortcut_idx:
            print('[' + ch + ']', end='')
        else:
            print(ch, end='')
    print()



