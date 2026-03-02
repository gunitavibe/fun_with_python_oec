"""
File Handling Demo for Evolution Simulation
"""
#r=read file
#w = write
#a = use to add new data in file
#r+ = use for read and write in file
# Read file
with open("11_evolution.txt", "r") as file:
    content = file.read()
    print("Original Content:")
    print(content)

# Write file (append mode)
with open("11_evolution.txt", "a") as file:
    file.write("\ added in 12evolution.py")

print("Data appended successfully.")