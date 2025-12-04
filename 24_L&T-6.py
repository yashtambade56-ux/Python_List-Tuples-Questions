# Find the sum of all elements in a list without using sum().

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = 0
for number in numbers:
    total += number

print("The sum of all elements is:", total)