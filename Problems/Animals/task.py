animals = list()
# read animals.txt
with open('animals.txt', 'rt') as in_file:
    for line in in_file:
        # animals.append(line)
        animals.append(line.rstrip())
# and write animals_new.txt
with open('animals_new.txt', 'wt') as out_file:
    out_file.write(' '.join(animals))
    # out_file.close()
