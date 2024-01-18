a = []
for _ in range(int(input())):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)

    a.append((name, kor, eng, math))

a.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in a:
    print(name)
