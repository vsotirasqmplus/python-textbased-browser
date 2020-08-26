dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
errs = 0
for word in sentence:
    if word not in dictionary:
        print(word)
        errs += 1
if errs == 0:
    print('OK')
