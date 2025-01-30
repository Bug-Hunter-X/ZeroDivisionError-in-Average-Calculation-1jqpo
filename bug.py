def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    return total / len(numbers)

# Example usage with potential error
averages = []
data_sets = [[1, 2, 3], [], [4, 5, 6], [7, 8]]
for data in data_sets:
    avg = calculate_average(data)
    averages.append(avg)
print(averages)