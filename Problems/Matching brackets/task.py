# put your python code here
letters = input()  # "((a + b)*c"
# letters = "((a + b)*c"
total = 0
dix = {'(': 1, ')': - 1}
for letter in letters:
    if letter in dix.keys():
        total += dix[letter]
        if total < 0:
            break

print('OK' if total == 0 else 'ERROR')
