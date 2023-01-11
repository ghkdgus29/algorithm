def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False

    return True


n = int(input())
given = list(map(int, input().split()))
num_of_prime = 0

for num in given:
    if is_prime(num):
        num_of_prime += 1

print(num_of_prime)
