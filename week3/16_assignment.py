"""
Assignment: List Operations in Python

Description:
This program demonstrates various list operations in Python such as:
- Creating a list
- Adding elements (append, insert, extend)
- Accessing elements (indexing, slicing)
- Updating elements
- Removing elements
- Sorting a list
- Clearing a list
"""

# Step 1: Create a list
orders = ["Milk", "Bread", "Eggs"]
print("Initial Orders:", orders)

# Step 2: Add an item using append()
orders.append("Butter")
print("After append():", orders)

# Step 3: Insert an item at a specific position
orders.insert(1, "Fruits")
print("After insert():", orders)

# Step 4: Extend the list with another list
partner_orders = ["Rice", "Oil"]
orders.extend(partner_orders)
print("After extend():", orders)

# Step 5: Access the first element
print("First item:", orders[0])

# Step 6: Slice the list (first three items)
batch_orders = orders[0:3]
print("Batch Orders (first 3 items):", batch_orders)

# Step 7: Update an element
orders[orders.index("Milk")] = "Almond Milk"
print("After updating Milk:", orders)

# Step 8: Remove an item
orders.remove("Bread")
print("After remove():", orders)

# Step 9: Sort the list
orders.sort()
print("After sort():", orders)

# Step 10: Clear the list
orders.clear()
print("After clear():", orders)