# +Index - 0 1 2
# -Index - -3 -2 -1

courses = ["Huddy", "Chari", "Beb", "gaga", "gaga"]
food = ["cat", "dog"]
alphabet = ["W", "A", "S", "B", "C", "F"]
number = ["toto", "chen", "dish", ["andrew", "tristan"]]


courses.insert(0, "julia")
courses.insert(1, "genshin")
courses.remove("Huddy")
courses.remove("Chari")
courses.pop(1)
food.reverse()
alphabet.sort(reverse = True)

print(food)
print(courses)
print(alphabet)
print(number[3][0])