grocery_list = [
    "Milk",
    "Bread",
    "Eggs",
    "Peanut Butter",
    "Jelly"
]

print(grocery_list)

grocery_list[grocery_list.index("Peanut Butter")] = "Almond butter"

print(grocery_list)

grocery_list.pop(grocery_list.index("Jelly"))

print(grocery_list)

grocery_list.append("Coffee")

print(grocery_list)