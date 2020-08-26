from collections import deque
n = int(input())
lines = [input() for _ in range(n)]
stack = deque()
read_books = deque()
for line in lines:
    words = line.split()
    action = words.pop(0)
    # print(action)
    title = ' '.join(words)
    if action == 'BUY':
        stack.append(title)
    if action == 'READ':
        read_books.append(stack.pop())

for book in read_books:
    print(book)
