# Multiply all elements of a list.

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

product = 1
for number in numbers:
    product *= number

print("The product of all elements is:", product)