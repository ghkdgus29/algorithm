n = int(input())
people = list(map(int, input().split()))
people.sort()

wait = 0
total_wait = 0
for person in people:
    wait += person
    total_wait += wait

print(total_wait)
