from random import randint

def draw_letters():
    
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
    letter_pool = []
    for letter in LETTER_POOL:
        for _ in range(LETTER_POOL[letter]):
            letter_pool.append(letter)

    drawn_letters = []
    for _ in range(10):
        new_letter = letter_pool[randint(0, len(letter_pool) - 1)]
        letter_pool.remove(new_letter)
        drawn_letters.append(new_letter)

    return drawn_letters

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    letters = letter_bank[:]
    for letter in uppercase_word:
        if letter not in letters:
            return False
        else:
            letters.remove(letter)
    return True

def score_word(word):
    points = 0

    if len(word) > 6:
        points += 8

    for char in word:
        char = char.upper()
        if char in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
            points += 1
        elif char in ["D", "G"]:
            points += 2
        elif char in ["B", "C", "M", "P"]:
            points += 3
        elif char in ["F", "H", "V", "W", "Y"]:
            points += 4
        elif char == "K":
            points += 5
        elif char in ["J", "X"]:
            points += 8
        else:
            points += 10

    return points

def get_highest_word_score(word_list):
    
    word_score_dict = {}
    for word in word_list:
        word_score_dict[word] = score_word(word)
    
    winning_score = list(word_score_dict.values())[0]
    for score in word_score_dict.values():
        if score > winning_score:
            winning_score = score

    winning_words_list = []
    for word in word_score_dict:
        if word_score_dict[word] == winning_score:
            winning_words_list.append(word)

    if len(winning_words_list) > 1:
        winning_word = winning_words_list[0]
        for word in winning_words_list:
            if len(word) >= 10:
                return word, winning_score
            elif len(word) < len(winning_word):
                winning_word = word
    else:
        return winning_words_list[0], winning_score
    
    return winning_word, winning_score

