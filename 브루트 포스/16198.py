def collect(sub_marbles: list, energy):
    if len(sub_marbles) <= 2:
        energy_candidiates.append(energy)
        return

    for i in range(1, len(sub_marbles) - 1):
        collect(sub_marbles[:i] + sub_marbles[i + 1:], energy + sub_marbles[i - 1] * sub_marbles[i + 1])


energy_candidiates = []

n = int(input())
marbles = list(map(int, input().split()))

collect(marbles, 0)

print(max(energy_candidiates))
