def pick(index, picks):
    if len(picks) == 6:
        print(*picks)
        return
    if index >= len(numbers):
        return

    pick(index + 1, picks + [numbers[index]])
    pick(index + 1, picks)


while True:
    numbers = list(map(int, input().split()))[1:]

    pick(0, [])
    print()
    if not numbers:
        break
