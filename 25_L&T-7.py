# Reverse a list using slicing.

elements = []
for i in range(5):
    elem = input(f"Enter element {i + 1}: ")
    elements.append(elem)

reversed_elements = elements[::-1]
print("Reversed list:", reversed_elements)