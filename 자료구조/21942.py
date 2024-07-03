import collections
import datetime
import sys

t, rent_period, penalty = input().split()
t = int(t)
rent_period = int(rent_period.split("/")[0]) * 60 * 24 + int(rent_period.split("/")[1].split(":")[0]) * 60 + int(
    rent_period.split("/")[1].split(":")[1])
penalty = int(penalty)

accounts = collections.defaultdict(dict)
penalty_accounts = collections.defaultdict(int)

for _ in range(t):
    borrow_day, borrow_time, product, name = sys.stdin.readline().split()

    ab_time = (datetime.datetime.strptime(borrow_day + " " + borrow_time, "%Y-%m-%d %H:%M") - datetime.datetime(2021, 1,
                                                                                                                1)).total_seconds() // 60
    ab_time = int(ab_time)

    if product in accounts and name in accounts[product]:  # 반납
        if ab_time - accounts[product][name] > rent_period:
            penalty_accounts[name] += (ab_time - accounts[product][name] - rent_period) * penalty
        del accounts[product][name]
    else:                                                   # 대여
        accounts[product][name] = ab_time

if not penalty_accounts:
    print(-1)

else:
    for key in sorted( penalty_accounts.keys()):
        print(key, penalty_accounts[key])

