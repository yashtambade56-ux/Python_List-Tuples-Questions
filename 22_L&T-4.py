# Merge two lists and sort them.

list1 = []
list2 = []
for i in range(5):
    num1 = int(input(f"Enter number {i + 1} for list 1: "))
    list1.append(num1)
for i in range(5):
    num2 = int(input(f"Enter number {i + 1} for list 2: "))
    list2.append(num2)

merged_list = list1 + list2
merged_list.sort()
print("The merged and sorted list is:", merged_list)