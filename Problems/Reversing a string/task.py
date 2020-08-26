n = int(input())

my_stack = [ input().strip() for _ in range(n)]

for _ in range(n):
    print(my_stack.pop())

