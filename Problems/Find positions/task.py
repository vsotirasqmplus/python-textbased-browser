# put your python code here
line = input().split()
number = str(int(input()))
offset = 0
indices = ''
for i, n in enumerate(line):
    if n == number:
        indices += str(i) + ' '
if indices == '':
    print("not found")
else:
    print(indices)
