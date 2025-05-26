from collections import deque

d = deque([17, 55, 123])
d.append(7)
d.appendleft(100)
d.append(-91)
for _ in range(len(d)):
    print(d.popleft())