names = ("Eto" , "David", "John", "Mike", "Josh")

if len(names) < 10:
    names += ("Ambi", "Savvy", "Anthony", "Tyson")

for i in range(len(names)):
    print(names[i] + " is number " + str(i+1))
print("{} is the last person".format(names[len(names) - 1]))

new_list = list(sorted(names))

names_2 = list(names)

names_2.sort()

print(names_2)


# for j in range(len(new_list_2)):
#     j % 2 == 0
#     print(new_list_2[i].lower())

print(new_list)