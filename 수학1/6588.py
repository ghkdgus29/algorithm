import sys

MAX = 1000000
prime_check = [True] * (MAX + 1)
prime_check[0] = False
prime_check[1] = False

for i in range(2, MAX + 1):
    if prime_check[i]:
        for j in range(i + i, MAX + 1, i):
            prime_check[j] = False


def find_prime_sum(input_number):
    for i in range(2, input_number // 2 + 1):
        if prime_check[i] and prime_check[input_number - i]:        # i + (input_number - 1) = input_number
            print(str(input_number) + " = " + str(i) + " + " + str(input_number - i))
            return


while True:
    input_number = int(sys.stdin.readline().rstrip())

    if input_number == 0:
        break

    find_prime_sum(input_number)
