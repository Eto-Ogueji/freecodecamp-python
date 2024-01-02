# sort a list w/o modifying the original list
items = ["Roger", "bob", "Beau", "Quincy"]

print(sorted(items, key=str.lower))

print(items)