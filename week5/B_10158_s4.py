import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

tp = (p + t) // w
tq = (q + t) // w

