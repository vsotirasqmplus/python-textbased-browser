words = input().split()
found = list()
for word in words:
    if word[-1] == 's':
        found.append(word)
print('_'.join(found))
