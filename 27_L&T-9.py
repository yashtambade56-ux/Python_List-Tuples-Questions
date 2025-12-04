# Find the index of a value in a tuple (handle value not present).

values = (10, 20, 30, 40, 50)
try:
    target = int(input("Enter a value to find its index: "))
    index = values.index(target)
    print(f"The index of {target} is: {index}")
except ValueError:
    print(f"{target} is not present in the tuple.")