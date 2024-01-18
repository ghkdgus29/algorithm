a = []

for i in range(int(input())):
    age, name = input().split()
    age = int(age)
    a.append((age, i, name))

a.sort()

for age, _, name in a:
    print(age, name)
