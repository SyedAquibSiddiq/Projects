import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json", "r"))


def func_ask():

    print("____AQUIB'S DICTIONARY____")
    ask_word = input("Enter The Word: ")
    output = definitions(ask_word)
    # output returns a list of definitions, so extracting it out from the list
    if type(output) == list:
        for sentence in output:
            print("*", sentence)
    else:
        # if output is not a list, printing the output without iterating through it
        print(output)
        return "Happy Finding :)"


def definitions(word):

    word = word.lower()
    # if word.lower() matches the word in data returning the data[word]
    if word in data:
        return data[word]
    # checking for exact noun like (Delhi) in the data.keys()
    elif word.title() in data:
        return data[word.title()]
    # checking for words with all caps like (USA) in the data.keys()
    elif word.upper() in data:
        return data[word.upper()]
    # checking for posiblities
    elif len(gcm(word, data.keys())) > 0:
        check = input(
            f"Well Did You Mean {gcm(word, data.keys())[0]}? If Yes Enter 'Y' Else Enter 'N': "
        )
        if check.lower() == "y":
            return data[gcm(word, data.keys())[0]]
        elif check.lower() == "n":
            return "Sorry! Not In The Dictionary."
        else:
            return f"Your Word{word} Not In AQUIB'S DICTIONARY"
    else:
        last_check = input(
            f"Your Word {word} Is Not In The Dictionry! \nDo You Want To Search? You Have a Chance....Type 'yes/y' or 'no/n': "
        )
        if last_check.lower() == "yes" or last_check.lower() == "y":
            chance = 0
            chance += 1
            print(chance)
            if chance > 1:
                return f"Your Word {word} Is Not In AQUIB'S DICTIONARY"
            else:
                # if the user want to search again repeating the program by calling func_ask()
                return func_ask()
        elif last_check.lower() == "no" or last_check.lower() == "n":
            return f"Your Word {word} Is Not In AQUIB'S DICTIONARY"
        else:
            return "Your Word Is Out Of This Dictionary :("


func_ask()
