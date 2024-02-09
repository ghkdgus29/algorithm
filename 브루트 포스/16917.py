seasoned_price, fried_price, mixed_price, seasoned_cnt, fried_cnt = map(int, input().split())

ans = 0
if mixed_price * 2 < seasoned_price + fried_price:
    min_cnt = min(seasoned_cnt, fried_cnt)
    ans += min_cnt * (mixed_price * 2)
    seasoned_cnt -= min_cnt
    fried_cnt -= min_cnt

    if seasoned_cnt > 0:
        if seasoned_price > mixed_price * 2:
            seasoned_price = mixed_price * 2
        ans += seasoned_price * seasoned_cnt

    else:
        if fried_price > mixed_price * 2:
            fried_price = mixed_price * 2
        ans += fried_price * fried_cnt

else:
    ans = seasoned_cnt * seasoned_price + fried_cnt * fried_price

print(ans)
