# Input 10 numbers into a list and print the second largest.

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

numbers.sort()
print("The second largest number is:", numbers[-2])