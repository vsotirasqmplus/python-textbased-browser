def range_sum(numbers, start, end):
    total = 0
    start = int(start)
    end = int(end)
    for n in numbers:
        n = int(n)
        if start <= n <= end:
            total += n
    return total


input_numbers = input().split()  # ...
a, b = input().split()
print(range_sum(input_numbers, a, b))
