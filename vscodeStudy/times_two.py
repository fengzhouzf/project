numbers = [2, 4, 6, 8]

def times_two(values):
    total = 0
    for num in numbers:
        total += num * 2
    return total

print(times_two(numbers))