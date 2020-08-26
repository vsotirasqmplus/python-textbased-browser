numbers = [int(char) for char in input()]
print([sum(numbers[0:i + 1]) for i in range(len(numbers))])
