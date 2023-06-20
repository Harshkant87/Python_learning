# 1. old usual method
temps = [220, 340, 346, 215]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# 2. by using list comprehension
new_temps_list = [temp / 10 for temp in temps]
print(new_temps_list)

# 3. Conditionals in list comprehension
temps = [221, 334, 356, -765, 230]
new_temps_list = [temp / 10 for temp in temps if temp > 0]
print(new_temps_list)

# 4. if you want to use if else then
temps = [221, 334, 356, -765, 230]
new_temps_list = [temp / 10 if temp > 0 else 0 for temp in temps]
print(new_temps_list)
