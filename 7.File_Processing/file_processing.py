# 1. Read file
my_file = open("cricketer.txt")
# print(my_file.read())

# 2. you can save content of variable as well
content = my_file.read()
print(content)

# 3. Close your file
my_file.close()

# 4. Open your file with 'with', it autocloses the file
with open("cricketer.txt") as my_file:
    content = my_file.read()

print(content)

# 5. opening file from different directory
# with open("6.Functions_L2/ipl_teams.txt") as file:
#     content = file.read()

# print(content)

# 6. Writing in a file
with open("vegetables.txt", "w") as file:
    file.write("Tomato")

# 7. appending in a file
with open("vegetables.txt", "a") as file:
    file.write("\nPotato")