octa = list(map(int, input()))

binary = []     # 작은 자리수 부터 저장된다. (little endian)

for oct in reversed(octa):
    for i in range(3):
        if oct > 0:
            binary.append(oct % 2)
            oct //= 2
        else:
            binary.append(0)

for bin in reversed(binary):    # 큰 자리수부터 시작하는 0을 제거하기 위한 동작
    if bin != 0:
        break
    binary.pop()

binary.reverse()
if binary:
    print(''.join(map(str, binary)))
else:
    print(0)                    # 0일 경우엔 그냥 0 출력
