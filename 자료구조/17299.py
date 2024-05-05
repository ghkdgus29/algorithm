import collections

length = int(input())
given = list(map(int, input().split()))

counter = collections.Counter(given)       # counter 를 사용하여 개수를 셈
index_stack = []
ans = [-1] * length

for i in range(length):
    while index_stack and counter[given[index_stack[-1]]] < counter[given[i]]:
        ans[index_stack.pop()] = given[i]
    index_stack.append(i)

print(*ans)
