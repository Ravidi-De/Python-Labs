for i in range(8):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Sort the numbers using the sorted function
sorted_numbers = sorted(numbers)

# Print the sorted numbers
print("Sorted numbers:")
for num in sorted_numbers:
    print(num)
