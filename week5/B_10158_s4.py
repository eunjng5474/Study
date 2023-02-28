import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

while t:
    t -= 1
    p += 1
    q += 1
    # if p