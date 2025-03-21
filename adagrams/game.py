from random import randint

LETTER_POOL = {
    "A": {"count": 9, "score": 1},
    "B": {"count": 2, "score": 3},
    "C": {"count": 2, "score": 3},
    "D": {"count": 4, "score": 2},
    "E": {"count": 12, "score": 1},
    "F": {"count": 2, "score": 4},
    "G": {"count": 3, "score": 2},
    "H": {"count": 2, "score": 4},
    "I": {"count": 9, "score": 1},
    "J": {"count": 1, "score": 8},
    "K": {"count": 1, "score": 5},
    "L": {"count": 4, "score": 1},
    "M": {"count": 2, "score": 3},
    "N": {"count": 6, "score": 1},
    "O": {"count": 8, "score": 1},
    "P": {"count": 2, "score": 3},
    "Q": {"count": 1, "score": 10},
    "R": {"count": 6, "score": 1},
    "S": {"count": 4, "score": 1},
    "T": {"count": 6, "score": 1},
    "U": {"count": 4, "score": 1},
    "V": {"count": 2, "score": 4},
    "W": {"count": 2, "score": 4},
    "X": {"count": 1, "score": 8},
    "Y": {"count": 2, "score": 4},
    "Z": {"count": 1, "score": 10}
    }

def draw_letters():
    tiles = []
    hand = []

    for letter, letter_data in LETTER_POOL.items():
        for i in range(letter_data["count"]):
            tiles.append(letter)

    while len(hand) < 10:
        tile_index = randint(0, len(tiles) - 1)
        tile = tiles[tile_index]
        hand.append(tile)
        tiles.remove(tile)

    return hand

def uses_available_letters(word, letter_bank):
    letter_bank = letter_bank.copy()

    for letter in word.upper():
        if letter in letter_bank:
            letter_bank.remove(letter)
        else:
            return False

    return True

def score_word(word):
    score = 0

    if not word:
        return 0
    
    if len(word) > 6:
        score += 8

    for letter in word.upper():
        score += LETTER_POOL[letter]["score"]
    
    return score

def get_highest_word_score(word_list):
    max_score = score_word(word_list[0])
    highest_word = word_list[0]

    for current_word in word_list:
        current_score = score_word(current_word)

        if current_score == max_score:
            if len(highest_word) == 10:
                continue
            elif len(current_word) == 10:
                highest_word = current_word
            elif len(highest_word) > len(current_word):
                highest_word = current_word

        elif current_score > max_score:
            max_score = current_score
            highest_word = current_word

    return highest_word, max_score
