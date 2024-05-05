length = int(input())
given = list(map(int, input().split()))

index_stack = []        # 인덱스를 저장
ans = [-1] * length

for i in range(length):
    while index_stack and given[index_stack[-1]] < given[i]:
        ans[index_stack.pop()] = given[i]
    index_stack.append(i)

print(*ans)

