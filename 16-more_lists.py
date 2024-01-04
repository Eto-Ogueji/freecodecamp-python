items = ["Roger", 1, "Syd", True, "Eto", 4]

print("Roger" in items) # True

# string indexes can be updated
items[2] = "Beau" # no more "Syd"

# slicing
print(items[0:3])

# print length of list
print(len(items))

# add value at the end of the list
items.append("Judah")

# add more than one value
items.extend(["David", 5])

# remove value
items.remove("Beau") # removes "Beau"

# removes last item from list and returns it
print(items.pop())

# check list after removing an item
print(items)

# add items at an index without replacing the original value at the index
items.insert(2, "Savage")

# sort list
items.sort()
print(items)


names = ["Eto", "Johnpaul", "Ogueji"]