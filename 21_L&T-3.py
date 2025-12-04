# Count how many times each item appears in a list.

items = []
for i in range(10):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)
item_count = {}
for item in items:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1

for item, count in item_count.items():
    print(f"{item}: {count}")