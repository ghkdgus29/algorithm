n = int(input())
number_of_5 = 0

for i in range(2, n + 1):
    num = i

    while num > 1:              # 인수 5의 개수 세기 (2의개수는 5의개수보다 항상 많다.)
        if num % 5 != 0:
            break
        num /= 5
        number_of_5 += 1

print(number_of_5)
