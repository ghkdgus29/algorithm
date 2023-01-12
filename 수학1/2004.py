def cal(number):
    number_of_2 = 0
    number_of_5 = 0

    divisor = 2
    while number >= divisor:                    # 인수 2의 개수
        number_of_2 += number // divisor
        divisor *= 2

    divisor = 5
    while number >= divisor:                    # 인수 5의 개수
        number_of_5 += number // divisor
        divisor *= 5

    return number_of_2, number_of_5


n, m = map(int, input().split())

numerator_of_2, numerator_of_5 = cal(n)
first_denominator_of_2, first_denominator_of_5 = cal(m)
second_denominator_of_2, second_denominator_of_5 = cal(n - m)

print(min(numerator_of_2 - first_denominator_of_2 - second_denominator_of_2,
          numerator_of_5 - first_denominator_of_5 - second_denominator_of_5))
