from random import randint

def draw_letters():
    # Borrowed from test_wave_01.py; used to build expanded letter pool list.
    LETTER_POOL_FREQUENCIES = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }
    MAX_WORD_LENGTH = 10  # Maximum word length permitted.
    letter_pool = []  # will hold expanded letter pool list.
    # iterates through dictionary, adding the appropriate number of letters to
    # 'letter_pool' based on frequency:
    for letter, frequency in LETTER_POOL_FREQUENCIES.items():
        letter_pool += letter * frequency
    hand = []  # will hold the player's drawn hand.

    past_indices = []  # keeps track of what indices have been prev. selected.
    while len(hand) < MAX_WORD_LENGTH:  # loops until 'hand' is full.
        random_index = randint(0, len(letter_pool) - 1)  # selects random value
        # checks if current random_index has previously been selected:
        if random_index in past_indices:
            continue
        # if above check passes, adds letter to 'hand' and current index to
        # 'past_indices':
        hand += letter_pool[random_index]
        past_indices.append(random_index)

    return hand

def uses_available_letters(word, letter_bank):
    formatted_word = word.upper() # formats 'word' to all uppercase letters.
    # builds 'letter_bank_count' to keep track of letters in the bank:
    letter_bank_count = {}
    for letter in letter_bank:
        if letter not in letter_bank_count:
            letter_bank_count[letter] = 1  # adds new key:value if not present
        else:
            letter_bank_count[letter] += 1  # adds to value if key is present
    # builds 'word_letter_count' to keep track of letters in word:
    word_letter_count = {}
    for letter in formatted_word:
        if letter not in word_letter_count:
            word_letter_count[letter] = 1
        else:
            word_letter_count[letter] += 1
        # checks if letter is present in letter bank OR if a letter has been
        # used more than the number of times it appears in the bank; returns
        # False if either condition is true:
        if (letter not in letter_bank
            or word_letter_count[letter] > letter_bank_count[letter]):
            return False

    return True  # f(x) returns True if checks above pass.

def score_word(word):
    # dictionary of letters and their point values:
    letter_values = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R':1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    MIN_BONUS_LENGTH = 7  # minimum word length for length point bonus
    WORD_LENGTH_BONUS = 8  # amount of points awarded for length bonus
    score = 0

    for letter in word:
        formatted_letter = letter.upper()  # formats letter to uppercase

        score += letter_values[formatted_letter]  # adds points to 'score'
    # adds length bonus if word meets requirement:
    if len(word) >= MIN_BONUS_LENGTH:
        score += WORD_LENGTH_BONUS

    return score

def get_highest_word_score(word_list):
    # dictionary of letters and their point values:
    letter_values = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R':1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    MIN_BONUS_LENGTH = 7  # minimum word length for point bonus
    WORD_LENGTH_BONUS = 8  # amount of points awarded for length bonus.
    MAX_WORD_LENGTH = 10  # maximum word length permitted.
    winning_word = ""  # tracks the winning word
    highest_score = 0  # tacks the highest score

    for word in word_list:
        current_score = 0  # tracks the current score of a given word
        # this for loop handles calculating the current word's score:
        for letter in word:
            current_score += letter_values[letter]
        # adds the length bonus for 7 letter words or longer:
        if len(word) > MIN_BONUS_LENGTH:
            current_score += WORD_LENGTH_BONUS
        # this outer if/elif block checks current score against the highest;
        # if greater, assigns word to winning_word & currecnt_score to
        # highest_score...
        if current_score > highest_score:
            winning_word = word
            highest_score = current_score
        # ... but if equal, the inner if/elif block within elif executes
        # depending on lengths:
        elif current_score == highest_score:
            # if word is of length 10 AND the current winning_word isn't
            # already 10 letters long:
            if (len(word) == MAX_WORD_LENGTH
                and len(winning_word) != MAX_WORD_LENGTH):
                winning_word = word
                highest_score = current_score
            # if word length is shorter than winning_word AND winning_word
            # isn't 10 letters long:
            elif (len(word) < len(winning_word)
                  and len(winning_word) != MAX_WORD_LENGTH):
                winning_word = word
                highest_score = current_score

    return winning_word, highest_score
