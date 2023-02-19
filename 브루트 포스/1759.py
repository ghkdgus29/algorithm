# 모음 1개, 자음 2개, 오름차순

vowel = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}


def make_password(vowel_count, consonant_count, count, index):
    if count == pick:
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(ans))
        return

    for i in range(index, given):
        ans[count] = a[i]
        if a[i] in vowel.keys():
            make_password(vowel_count + 1, consonant_count, count + 1, i + 1)
        else:
            make_password(vowel_count, consonant_count + 1, count + 1, i + 1)


pick, given = map(int, input().split())
a = sorted(list(input().split()))
ans = [0] * pick

make_password(0, 0, 0, 0)
