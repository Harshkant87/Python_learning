import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.upper()
    if word in data:
        result = data[word]
        return result
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist please double check it!"
        else:
            return "Kindly enter valid input!"
    else:
        return "The word does not exist!"

while(True):
    message = '''Welcome to my Thesaurus!
                 Enter the word to know its meaning.
                 Type exit() to close this program.'''
    print(message)
    word = input("Enter word: ")
    if word == "exit()":
        break
    print(translate(word))
    print("****************************************\n")