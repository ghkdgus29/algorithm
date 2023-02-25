# def check():
#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total += ans[j]
#             if sign_matrix[i][j] == "0":
#                 if total != 0:
#                     return False
#             elif sign_matrix[i][j] == "-":
#                 if total >= 0:
#                     return False
#             elif sign_matrix[i][j] == "+":
#                 if total <= 0:
#                     return False
#     return True
#
#
# def find(index):
#     if index == n:
#         return check()
#
#     for i in range(-10, 11):          # 모든 범위의 숫자를 넣고 탐색
#         ans[index] = i
#         if find(index + 1):
#             return True               # 정답이 하나라도 나오면 for 문 종료
#     return False                      # 21^10 경우의 수 -> 시간초과

# def check():
#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total += ans[j]
#             if sign_matrix[i][j] == "0":
#                 if total != 0:
#                     return False
#             elif sign_matrix[i][j] == "-":
#                 if total >= 0:
#                     return False
#             elif sign_matrix[i][j] == "+":
#                 if total <= 0:
#                     return False
#     return True
#
#
# def find(index):
#     if index == n:
#         return check()
#
#     if sign_matrix[index][index] == "0":            # sign_matrix[index][index]는 단 한개의 정수이므로, index 번째 정수의 부호를 결정한다.
#         ans[index] = 0
#         if find(index + 1):
#             return True
#
#     for i in range(1, 11):
#         if sign_matrix[index][index] == "-":        # sign_matrix[index][index]는 단 한개의 정수이므로, index 번째 정수의 부호를 결정한다.
#             ans[index] = i * -1
#         else:
#             ans[index] = i
#
#         if find(index + 1):
#             return True               # 정답이 하나라도 나오면 for 문 종료
#     return False                      # 10^10 시간 초과

def check(index):
    total = 0
    for i in range(index, -1, -1):              # 인덱스번째 열 성분만 모두 조사한다.
        total += ans[i]
        if sign_matrix[i][index] == "0":
            if total != 0:
                return False
        elif sign_matrix[i][index] == "-":
            if total >= 0:
                return False
        elif sign_matrix[i][index] == "+":
            if total <= 0:
                return False
    return True


def find(index):
    if index == n:
        return True                                     # 조건 검사를 중간에 하기 때문에 n 길이 ans배열을 만들었다면, 정답 완성을 의미

    if sign_matrix[index][index] == "0":                # sign_matrix[index][index]는 단 한개의 정수이므로, index 번째 정수의 부호를 결정한다.
        ans[index] = 0
        return check(index) and find(index + 1)         # 정수값을 정할 때 마다 조건을 만족했는지 검사한다.

    for i in range(1, 11):
        if sign_matrix[index][index] == "-":            # sign_matrix[index][index]는 단 한개의 정수이므로, index 번째 정수의 부호를 결정한다.
            ans[index] = i * -1
        else:
            ans[index] = i

        if check(index) and find(index + 1):            # 정수값을 정할 때 마다 조건을 만족했는지 검사한다.
            return True                                 # 정답이 하나라도 나오면 for 문 종료

    return False


n = int(input())
s = input()

sign_matrix = [[" "] * n for _ in range(n)]
ans = [0] * n

cnt = 0
for y in range(n):
    for x in range(y, n):
        sign_matrix[y][x] = s[cnt]
        cnt += 1

find(0)
print(*ans)
