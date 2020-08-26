text = input()
# text = text.lower()
words = text.split(maxsplit=20)
for word in words:
    is_add = False
    if word.count('.') == 2:
        is_add = True
    if word.lower().find('http') > -1 and len(word) > 4:
        is_add = True
    if word.lower().find('www') > -1 and len(word) > 3:
        is_add = True

    if is_add:
        print(word)
        is_add = False
