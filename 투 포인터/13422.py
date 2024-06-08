t = int(input())
for _ in range(t):
    n, cnt, limit = map(int, input().split())
    ans = 0
    house = list(map(int, input().split()))
    house = house + house[:cnt-1]
    steal = sum(house[:cnt])
    if steal < limit:
        ans += 1
    if n > cnt:
        for i in range(n-1):
            steal -= house[i]
            steal += house[i+cnt]
            if steal < limit:
                ans += 1
    print(ans)
        
