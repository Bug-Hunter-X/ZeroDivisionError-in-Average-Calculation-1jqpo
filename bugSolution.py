def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    return total / len(numbers)

# Example usage with potential error handled
averages = []
data_sets = [[1, 2, 3], [], [4, 5, 6], [7, 8]]
for data in data_sets:
    try:
        avg = calculate_average(data)
        averages.append(avg)
    except ZeroDivisionError:
        averages.append(0) # or handle appropriately
print(averages)