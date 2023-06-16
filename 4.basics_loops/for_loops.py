temperatures = [39.1, 40.6, 42.3, 45.3, 42.8]
for temperature in temperatures:
    print(round(temperature))

# 1. Similarly we can do for a string:
for letter in "MS Dhoni":
    print(letter) 

# 2. Iterate dictionaries: 
eng_to_hindi = {
    "Hello" : "Namaste",
    "Breakfast" : "Nasta",
    "Currency" : "Mudra",
    "School" : "Vidyalaya"
}

for item in eng_to_hindi.items():
    print(item)

# 3. print either key or value:
for item in eng_to_hindi.keys():
    print(item)

for item in eng_to_hindi.values():
    print(item)
