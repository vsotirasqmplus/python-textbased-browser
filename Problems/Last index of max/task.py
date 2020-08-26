def last_indexof_max(numbers):
    # write the modified algorithm here
    max_v = ''
    idx = -1
    counter = -1
    for number in numbers:
        number = int(number)
        counter += 1
        if max_v == '':
            max_v = number
        if number >= max_v:
            max_v = number
            idx = counter
    return idx * 1

# print(last_indexof_max("8 11 15 15 15 12".split()))
