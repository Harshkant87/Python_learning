import json

data = json.load(open("data.json"))

def translate(word):
    result = data[word.upper()]
    return result

word = input("Enter word: ")
print(translate(word))
