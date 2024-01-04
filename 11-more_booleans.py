done = True

done2 = ""

print(type(done) == bool) # True
print(type(done2) == bool) # False

if done:
    print("yes")
else:
    print("no") # prints yes

if done2:
    print("yes")
else:
    print("no") # prints no


book_1_read = True
book_2_read = False

# any returns true if any the values are true
read_any_book = any([book_1_read, book_2_read])
print(read_any_book) # True

# all returns true if all the values are true
read_any_book2 = any([book_1_read, book_2_read])
print(read_any_book2) # False