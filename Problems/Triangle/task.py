height = int(input())
for it in range(height):
    print(' ' * (height - it - 1) + '#' * ((it * 2) + 1))
