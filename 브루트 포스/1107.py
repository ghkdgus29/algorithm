# import sys
#
# NOT_MATCHED = 500001
#
# def list2int(li: list):
#     sum = 0
#     digit = 1
#     while li:
#         sum += li.pop() * digit
#         digit *= 10
#     return sum
#
#
# wanted_ch = int(input())
# if int(input()) == 0:
#     breakdown = []
# else:
#     breakdown = list(map(int, input().split()))
#
# current_ch = 100
#
# if current_ch == wanted_ch:
#     print(0)
#     sys.exit(0)
#
# want = list(map(int, str(wanted_ch)))
# lower_moved = []
# upper_moved = []
#
# if len(want) > abs(current_ch - wanted_ch):
#     print(abs(current_ch - wanted_ch))
#     sys.exit(0)
#
# push_count = len(want)
#
# for num in want:
#     if num not in breakdown:
#         lower_moved.append(num)
#         upper_moved.append(num)
#     else:
#         lower_num = num
#         while lower_num in breakdown:
#             lower_num -= 1
#         lower_moved.append(lower_num)
#         if lower_num < 0:
#             lower_moved.append(NOT_MATCHED)
#
#         upper_num = num
#         while upper_num in breakdown:
#             upper_num += 1
#         upper_moved.append(upper_num)
#         if upper_num > 9:
#             upper_moved.append(NOT_MATCHED)
#
# push_count += min(abs(wanted_ch - list2int(lower_moved)), abs(wanted_ch - list2int(upper_moved)))
# print(push_count)
