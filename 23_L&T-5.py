# Convert a list to tuple and tuple back to list.

elements = []
for i in range(5):
    elem = input(f"Enter element {i + 1}: ")
    elements.append(elem)

elements_tuple = tuple(elements)
print("Tuple:", elements_tuple)

elements_list = list(elements_tuple)
print("List:", elements_list)