digits = list(input())
digits.sort(reverse=True)

number = int(''.join(digits))

if number % 30 != 0:
    print(-1)
else:
    print(number)
