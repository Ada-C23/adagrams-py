from random import randint

LETTER_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
            "C", "C", "D", "D", "D", "D",
            "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
            "F", "F", "G", "G", "G", "H", "H",
            "I", "I", "I", "I", "I", "I", "I", "I", "I",
            "J", "K", "L", "L", "L", "L",
            "M", "M", "N", "N", "N", "N", "N", "N",
            "O", "O", "O", "O", "O", "O", "O", "O",
            "P", "P", "Q",
            "R", "R", "R", "R", "R", "R",
            "S", "S", "S", "S",
            "T", "T", "T", "T", "T", "T",
            "U", "U", "U", "U", "V", "V",
            "W", "W", "X", "Y", "Y", "Z"]

SCORE_CHART = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" :10,
        "Z" :10
    }

def draw_letters():
    tile_hand = []
    LETTER_POOL_copy = LETTER_POOL.copy()
    while len(tile_hand) < 10:
            index = randint(0,len(LETTER_POOL_copy) -1)
            tile_hand.append(LETTER_POOL_copy[index])
            LETTER_POOL_copy.remove(LETTER_POOL_copy[index])

    return tile_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_count = {}
    
    for i in letter_bank:
        if i not in letter_bank_count:
            letter_bank_count[i] = 1
        else:
            letter_bank_count[i] += 1

    for char in word:
        if char in letter_bank and letter_bank_count[char] > 0:
            letter_bank_count[char] -= 1
        
        else: 
            return False
        
    return True

def score_word(word):
    total_score = 0
    word = word.upper()

    if word == "":
        total_score = 0

    if len(word) >= 7:
        total_score += 8

    for char in word:
        letter_points = SCORE_CHART[char]
        total_score += letter_points     

    return total_score

def get_highest_word_score(word_list):
    winning_word = word_list[0]
    winning_word_score = score_word(word_list[0])
    
    for index in range(1, len(word_list)):
        contender_word = word_list[index]
        contender_word_score = score_word(contender_word)
        
        if winning_word_score > contender_word_score:
            winning_word = winning_word

        elif winning_word_score < contender_word_score:
            winning_word = contender_word

        elif winning_word_score == contender_word_score:
            if len(winning_word) >= 10:
                winning_word = winning_word
            elif len(word_list[index]) >= 10:
                winning_word = contender_word
            elif len(winning_word) < len(contender_word):
                winning_word = winning_word
            else:
                winning_word = contender_word

        winning_word_score = score_word(winning_word)
    
    result = (winning_word, winning_word_score)

    return result