words = input().split()
print(words.pop(0).lower() + ''.join(word.capitalize() for word in words))
