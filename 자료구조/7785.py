n = int(input())
attendance = set()
for _ in range(n):
    name, command = input().split()
    if command == 'enter':
        attendance.add(name)
    else:
        attendance.remove(name)

for name in sorted(attendance, reverse=True):
    print(name)
