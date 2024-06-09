# x -> y 번 까지의 악보를 순서대로 연주
# 현재 악보 > 다음 악보 -> 실수 발생
# 마지막 연주에선 절대 실수 x
# 실수 몇 번?
import sys

n = int(input())
songs = list(map(int, input().split()))
q = int(input())
mistake = [0]

for i in range(n - 1):
    mistake.append(mistake[-1] + (songs[i] > songs[i + 1]))

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(mistake[y - 1] - mistake[x - 1])
