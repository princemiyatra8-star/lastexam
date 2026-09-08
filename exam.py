print("Welcome to Inventory List Analyzer!")

item_names = []
item_quantities = []
category_set = set()

while True:

    name = input("\nEnter item name: ")

    category = input("Enter category: ")

    quantity = input("Enter quantity: ")

    while quantity.isdigit() == False:
        print("Please enter a valid number.")
        quantity = input("Enter quantity: ")

    quantity = int(quantity)

    item_names.append(name)
    item_quantities.append(quantity)
    category_set.add(category)

    choice = input("\nDo you want to add more items? (y/n): ")

    if choice != "y":
        break


print("\n----------- INVENTORY SUMMARY -------------")


# Total items


total_items = len(item_names)

print("\nTotal Items:", total_items)
print("Items entered:", item_names)


# Total quantity


total_quantity = sum(item_quantities)

print("\nTotal Quantity in Stock:", total_quantity)

print("Explanation:")

for i in range(total_items):
    print(item_quantities[i], end=" ")

print("=", total_quantity)


# Average quantity


average_quantity = total_quantity / total_items

print("\nAverage Quantity per Item:", average_quantity)

print("Explanation:", total_quantity, "/", total_items)


# Highest quantity


highest_quantity = max(item_quantities)

for i in range(total_items):

    if item_quantities[i] == highest_quantity:
        most_stocked_name = item_names[i]
        break

print("\nMost Stocked Item:", most_stocked_name)
print("Quantity:", highest_quantity, "units")


# Lowest quantity


lowest_quantity = min(item_quantities)

for i in range(total_items):

    if item_quantities[i] == lowest_quantity:
        least_stocked_name = item_names[i]
        break

print("\nLeast Stocked Item:", least_stocked_name)
print("Quantity:", lowest_quantity, "units")


print("\n================")


# Unique categories


print("\nUnique Categories in Inventory:")

for category in category_set:
    print(category)

print("Explanation: Set does not allow duplicate values.")


print("\n==================")


# Sort items by quantity


print("\nItems Sorted by Quantity (High to Low):")

sorted_names = item_names[:]
sorted_quantities = item_quantities[:]


for i in range(total_items):

    for j in range(total_items - 1):

        if sorted_quantities[j] < sorted_quantities[j + 1]:

            temp = sorted_quantities[j]
            sorted_quantities[j] = sorted_quantities[j + 1]
            sorted_quantities[j + 1] = temp

            temp = sorted_names[j]
            sorted_names[j] = sorted_names[j + 1]
            sorted_names[j + 1] = temp


for i in range(total_items):

    print(i + 1, ".", sorted_names[i], "-", sorted_quantities[i], "units")


print("\n===================")


# Categories in alphabetical order


print("\nCategories in Alphabetical Order:")

sorted_categories = sorted(category_set)

for i in range(len(sorted_categories)):

    print(i + 1, ".", sorted_categories[i])


print("\n------------ END OF REPORT --------------")