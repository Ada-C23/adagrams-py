from random import randint
# THis is a comment to push up!

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}


def draw_letters():
    letters_list = []
    extended_letters = []
    # this for loop, gooes through the letters/count dictionary and multiplies the amount of letters based on the count
    for letter, count in LETTER_POOL.items():
        extended_letters.extend([letter] * count)

    while len(letters_list) < 10:
        # we randomize the index of the extended letters list
        index = randint(0, len(extended_letters))-1
        letters_list.append(extended_letters.pop(index))
    return letters_list


def uses_available_letters(word, letter_bank):
    # we can make word be uppercase like the letter bank
    word = word.upper()
    # make copy of letter_bank to poke around with
    list_copy = letter_bank[:]
    # loop through word
    for letter in word:
        if letter in list_copy:
            list_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    # returns number representing points
    # each letter within word has a point value.
    # sum up all points in word to get word score
    # if word length is 7 - 10, word gets 8+ points
    # i want to make some lists of the points
    word = word.upper()
    value_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    value_2 = ["D", "G"]
    value_3 = ["B", "C", "M", "P"]
    value_4 = ["F", "H", "V", "W", "Y"]
    value_5 = ["K"]
    value_8 = ["J", "X"]
    value_10 = ["Q", "Z"]
    score = 0
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    for letter in word:
        if letter in value_1:
            score += 1
        elif letter in value_2:
            score += 2
        elif letter in value_3:
            score += 3
        elif letter in value_4:
            score += 4
        elif letter in value_5:
            score += 5
        elif letter in value_8:
            score += 8
        elif letter in value_10:
            score += 10
    return score


def get_highest_word_score(word_list):
    pass
# we can have a highest score variable that we will change to when we have the higher score than it already is
# we create a list to put the word, score since we cant mutate a tuple, and we can convert to a tuple later

    highest_score = 0
    future_tuple = ["word", "score"]
# loop through the word list
    for words in word_list:
        if score_word(words) > highest_score:
            highest_score = score_word(words)
            future_tuple[0] = words
            print(future_tuple[0])
            future_tuple[1] = highest_score
        elif score_word(words) == highest_score and len(future_tuple[0]) != 10:
            # print(len(words))
            # print(len(future_tuple[0]))
            if len(words) == 10:
                # print("WTF")
                future_tuple[0] = words
            elif len(words) < len(future_tuple[0]):

                future_tuple[0] = words
            else:
                continue
            # print(score_word(words), highest_score)
            # print(words, print(future_tuple[0]))

    results = tuple(future_tuple)
    print(results)
    return results
# word_list, is list of strings
# returns tuple, (winning word, score)
# index 0 = string of word
# iindex 1 = score of that word
# if tied: smallest word wins unless len is 10
# if same length and same score, first one returned


# word_input = "hello"
# letter_list = ["A", "C", "H", "Z", "E", "L", "F", "L", "C", "O"]
# uses_available_letters(word_input, letter_list)
word_list = ["AAAAAAAAAA", "BBBBBB"]
get_highest_word_score(word_list)
