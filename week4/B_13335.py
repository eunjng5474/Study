import sys
from collections import deque

n, w, L = map(int, input().split())
weight = list(map(int, sys.stdin.readline().split()))
bridge = deque()
wait = deque()
arrive = []

for w in weight:
    wait.append(w)

while len(arrive) != n:
    truck = wait.popleft()

