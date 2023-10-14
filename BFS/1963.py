import collections

n = int(input())

for _ in range(n):
    given, target = map(int, input().split())

    dist = [-1] * 10000

    primes = [True] * 10000

    for i in range(2, 5000):
        if primes[i]:
            for j in range(i + i, 10000, i):
                primes[j] = False

    queue = collections.deque()
    queue.append(given)
    dist[given] = 0

    while queue:
        pop = queue.popleft()

        for idx in range(4):
            str_number = list(str(pop))
            for i in range(10):
                str_number[idx] = str(i)

                number = int(''.join(str_number))
                if 1000 <= number <= 9999 and dist[number] == -1 and primes[number]:
                    dist[number] = dist[pop] + 1
                    queue.append(number)

    print(dist[target])
