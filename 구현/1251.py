# 단어를 세 개로 쪼갠 뒤 각 부분을 뒤집고 합쳤을 때 사전순으로 가장 앞서도록 하기

import itertools

s = input()

combinations = itertools.combinations([i for i in range(1, len(s))], 2)

ans = "z" * 51
for left, right in combinations:
    word = s[:left][::-1] + s[left:right][::-1] + s[right:][::-1]
    ans = min(ans, word)

print(ans)



