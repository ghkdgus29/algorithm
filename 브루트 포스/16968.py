def dfs(index):
    if index >= len(types):
        return 1

    cnt = 0
    if types[index] == 'c':
        for alp in alps:
            if index == 0 or alp != plate[index - 1]:
                plate[index] = alp
                cnt += dfs(index + 1)
    else:
        for num in nums:
            if index == 0 or num != plate[index - 1]:
                plate[index] = num
                cnt += dfs(index + 1)

    return cnt


types = input()

alps = [chr(ord('a') + i) for i in range(26)]
nums = list(range(10))
plate = [-1] * len(types)

print(dfs(0))
