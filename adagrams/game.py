from random import randint

LETTER_POOL = {
	    "A":9,"B":2,"C":2,"D":4,
	    "E":12,"F":2,"G":3,"H":2,
	    "I":9,"J":1,"K":1,"L":4,"M":2,
	    "N":6,"O":8,"P":2,"Q":1,
	    "R":6,"S":4,"T":6,"U":4,
	    "V":2,"W":2,"X":1,
	    "Y":2,"Z":1
	}

def draw_letters():
    letter_list = []
    letter_pool_list = []

    for alphabet, frenquency in LETTER_POOL.items():
        letter_pool_list.extend([alphabet] * frenquency)

    while len(letter_list) < 10:
        i = randint(0, len(letter_pool_list)-1)
        letter_list.append(letter_pool_list[i])
        letter_pool_list.pop(i)
    return letter_list  


def uses_available_letters(word, letter_bank):
    letter_bank_list = list(letter_bank)

    for alphabet in word.upper():
        if alphabet in letter_bank_list:
            letter_bank_list.remove(alphabet)
        else:
            return False
    return True


def score_word(word):
    SCORE_DICT = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    score = 0
    for alphabet in word.upper():
        score += score_dict[alphabet]
    if len(word) in {7,8,9,10}:
        score += 8
    return score



def get_highest_word_score(word_list):
    max_score = 0
    max_word = ""
    tie_words = []

    for word in word_list:
        if score_word(word) > max_score:
            max_score = score_word(word)
            max_word = word
            tie_words = [word]
        elif score_word(word) == max_score:
            tie_words.append(word)

    if len(tie_words) > 1:
        min_len =  len(tie_words[0])     
        for tie_word in tie_words:
            if len(tie_word) == 10:
                max_word = tie_word
                return (max_word,max_score)
            elif len(tie_word) < min_len:
                max_word = tie_word
                min_len = len(tie_word)

    return (max_word,max_score)