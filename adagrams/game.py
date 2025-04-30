from random import randint

HAND_SIZE = 10

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


score_chart = {'A':1,
                'B':3,
                'C':3,
                'D':2,
                'E':1,
                'F':4,
                'G':2,
                'H':4,
                'I':1,
                'J':8,
                'K':5,
                'L':1,
                'M':3,
                'N':1,
                'O':1,
                'P':3,
                'Q':10,
                'R':1,
                'S':1,
                'T':1,
                'U':1,
                'V':4,
                'W':4,
                'X':8,
                'Y':4,
                'Z':10
                }


def make_dict(array):
    '''
    Creates a dictionary of letters in the array as keys, and frequency of letters as values 
    input: a sting or a list of characters
    output: a dictionary of letters as keys, and frequency as values
    '''
    make_dict = {}
    for character in array:
        if character not in make_dict:
            make_dict[character] = 1
        else:
            make_dict[character] += 1
    return make_dict

# Easier way of doing it:
# for character in array:
#     make_dict[character] = make_dict.get(character, 0) + 1

def draw_letters():
    # Convert letter pool dictionary to a list with repeated letters 
    # the list above has 98 letters.
    # make a random selection out of 98 letters of pool list.
    # add the selected letter to the hand and add a counter that shows frequency of the letter in the hand
    # draw hand should be a dict array with k/v as letters / freq
    # check if freq of the selected letter is less than the freq of the pool
    # repeat this 10 times!
    # return a list of hand letters!
    
    letter_pool_list = []
    hand_dict = {}
    hand_list = []

    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool_list.append(letter)

    # for i in range(10): Can't use for loop in indetermined number of loops
    hand_counter = 1


    while hand_counter <= HAND_SIZE:  # using length len(hand_list) where you can instead of a counter
    # while hand_counter <= 10:  # 10 here withour comment and out of nowhere is called "magic number"
        draw = randint(0, 97)
        letter = letter_pool_list[draw]

        if letter not in hand_dict:
            hand_dict[letter] = 1
        else:
            if hand_dict[letter] < LETTER_POOL[letter]:
                hand_dict[letter] += 1
            else:
                continue
        
        hand_counter += 1 

    for letter, frequency in hand_dict.items():
        for i in range(frequency):
            hand_list.append(letter)

    return hand_list


def uses_available_letters(word, letter_bank):
    # first need to understand what are letters in word and how many of the letter do we have.
    # then I need to compare each letter with my draw bank:
    # if the letter in the word doesn't exist in the draw return false
    # if the letter is in the draw bank then check if the frequency in the word 
    # is more than the frequency of same letter in the draw bank
    
    word = word.upper()
    word_dict = make_dict(word)
    letter_bank_dict = make_dict(letter_bank)

    for character, frequency in word_dict.items():
        if  character not in letter_bank_dict:
            return False
        else:
            if frequency > letter_bank_dict[character]:
                return False
    return True
    

def score_word(word):
    # compare the letters in the word with the letters in score chart. 
    # add corresponding value to the total score
    # Chech if the length of word is more than 7 
    # (should we check if it is more than 10?)
    # return the total score


    # letter_bank = draw_letters() 
    word = word.upper()
    word_dict = make_dict(word)

    # if uses_available_letters(word, letter_bank): # No need to check!
    total_score = 0

    for letter, frequency in word_dict.items():
        total_score += score_chart[letter] * frequency

    if len(word) >= 7:
        total_score += 8

    return total_score
    

def get_highest_word_score(word_list):
    # we need to create a dictionary of words as keys and scores as values. (should we add the word length here?)
    # start the comparison: iterating over the dictionary and compare the values to get the highest score
    # within this loop we should consider the tie cases: with if statement, check the score is greater, or =
    # in case of equal scores: check the length of the words > smaller word is the winner!
    # BUT if length of the word is 10, and there are multiple tie score, 10 letter word is the winner!
    # if score and length are the same pich the first one as winner!
    
    highest_score = 0
    winner_word = None

    for word in word_list:
        score = score_word(word)

        if score > highest_score:
            winner_word = word
            highest_score = score
     
        elif score == highest_score:
            if len(word) == 10 and len(winner_word) != 10:
                winner_word = word              
            elif len(word) < len(winner_word) and len (winner_word) != 10:
                winner_word = word
            else:
                continue

    return (winner_word, highest_score)

# best_word = get_highest_word_score(["BBBBBB", "AAAAAAAAAA"])
# print(best_word[0])
# print(best_word[1])

# best_word = get_highest_word_score(["JQ", "FHQ", "AAAAAAAAAA", "BBBBBB", "TTTTTTTTTT"])
# print(best_word[0])
# print(best_word[1])

