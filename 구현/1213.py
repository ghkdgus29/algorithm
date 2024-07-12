# 짝수라면 각 원소 개수가 짝수여야 한다.
# 홀수라면 각 원소 개수가 짝수여야 하고, 하나만 홀수개의 원소를 갖는다.
import collections
import sys

# 사전순 출력

# 글자 개수 세기, counter 쓰기 -> 검사
# counter 키 정렬 후 순회
# 짝수개의 경우, 현재 key 개수의 반만큼 출력 -> 키 역순으로 정렬 후 순회하며 남은거 다 출력
# 홀수개의 경우, 홀수개 녀석을 찾아서 1빼고 fivot설정 -> 현재 key 개수의 반만큼 출력 -> fivot 출력 -> 키 역순으로 ..


s = input()
even = len(s) % 2 == 0
counter = collections.Counter(s)

ans = ""
if even:
    for key in sorted(counter.keys()):
        if counter[key] % 2 != 0:
            print("I'm Sorry Hansoo")
            sys.exit(0)

        for _ in range(counter[key] // 2):
            ans += key

    for key in sorted(counter.keys(), reverse=True):
        for _ in range(counter[key] // 2):
            ans += key

else:
    pivot = -1
    for key in sorted(counter.keys()):
        if counter[key] % 2 == 1:
            if pivot == -1:
                pivot = key
                counter[key] -= 1
            else:
                print("I'm Sorry Hansoo")
                sys.exit(0)

    for key in sorted(counter.keys()):
        for _ in range(counter[key] // 2):
            ans += key

    ans += pivot

    for key in sorted(counter.keys(), reverse=True):
        for _ in range(counter[key] // 2):
            ans += key

print(ans)
