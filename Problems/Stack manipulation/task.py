from collections import deque
queue = deque()
n = int(input().strip())
actions = [input().strip() for _ in range(n)]
for action in actions:
    elem = action.split()
    if elem[0] == 'PUSH':
        queue.append(elem[1])
    if elem[0] == 'POP':
        queue.pop()

for _ in range(len(queue)):
    print(queue.pop())
