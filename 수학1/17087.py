def gcd(a, b):
    if b <= 0:
        return a
    return gcd(b, a % b)


number_of_youngers, loc = map(int, input().split())
youngers_loc = list(map(int, input().split()))
distance = []

for younger_loc in youngers_loc:
    distance.append(abs(loc - younger_loc))

current_gcd = distance.pop()

while distance:                                        # 모든 거리들에 대해 gcd 반복
    current_gcd = gcd(current_gcd, distance.pop())

print(current_gcd)

