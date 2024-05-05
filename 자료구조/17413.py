given = list(input())
ans = ""
word = []
idx = 0

while idx < len(given):         # 모든 입력에 대해 처리
    if given[idx] == "<":
        if word:                                # 단어가 있는 경우 reverse 출력
            ans += "".join(reversed(word))
            word.clear()
        while given[idx] != ">":                # 태그가 닫힐 때 까지 순서대로 출력
            ans += given[idx]
            idx += 1
        ans += given[idx]
    elif given[idx] == " ":                     # 빈칸인 경우 이전 단어를 reverse 출력
        ans += "".join(reversed(word))
        ans += " "
        word.clear()
    else:                                       # 문자인 경우 단어리스트에 문자를 하나씩 추가
        word.append(given[idx])
    idx += 1

ans += "".join(reversed(word))                  # 마지막으로 남아있는 단어를 reverse 출력
print(ans)