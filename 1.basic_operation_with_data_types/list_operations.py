# 1. tells the operations that we can perform
s = ''
print(dir(s))

# 2. info regarding that particular method try it in shell
# help(s.replace())

# 3. append
temperatures = [33.2, 35.6, 39.6, 40.2]
temperatures.append(31.5)
print(temperatures)

# 4. clear method
temperatures.clear()
print(temperatures)

# 5. index method
temperatures = [33.2, 35.6, 39.6, 40.2]
print(temperatures.index(39.6))

# 6. accessing the item
print(temperatures.__getitem__(2))
print(temperatures[2])

# 7. slicing the list
temperatures = [33.2, 35.6, 39.6, 40.2, 31.5]
print(temperatures[1:4]) # from 1st index to 3rd index
print(temperatures[0:2]) # first two items of list
print(temperatures[len(temperatures) - 2: len(temperatures)]) # last two elements
print(temperatures[len(temperatures) - 2: ]) # last two items

# 8. list accessing and slicing with negative index
print(temperatures[-1]) # last item
print(temperatures[-4:-2])

# 9. Accessing string is same as the list
my_string = 'Hello'
print(my_string[-1]) # last character

# 10. in python list can contain different data types
temperatures.append(my_string)
print(temperatures)
i = temperatures.index('Hello')
print(temperatures[i][0]) 





