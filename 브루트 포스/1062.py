base = ["a", "n", "t", "i", "c"]

teach = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in base]

word_cnt, learn_limit = map(int, input().split())
words = [set(input()) for _ in range(word_cnt)]
check = [False] * 21
ans = [0]


def learn(index, learn_cnt):
    if learn_cnt == learn_limit:
        learned = set(base + [teach[i] for i in range(21) if check[i]])
        readable = 0
        for word in words:
            if word.issubset(learned):
                readable += 1

        ans.append(readable)
        return

    if index >= 21 or learn_cnt > learn_limit:
        return

    check[index] = True
    learn(index + 1, learn_cnt + 1)
    check[index] = False
    learn(index + 1, learn_cnt)


learn(0, 5)

print(max(ans))
