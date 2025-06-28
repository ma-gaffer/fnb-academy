
fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry"

print(fruits)

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.sort(reverse=True)
print(fruits)