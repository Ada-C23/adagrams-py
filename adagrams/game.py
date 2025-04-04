import random
from constants import SCORE_CHART, HAND_SIZE
from helper_functions import create_a_pile_of_letters, count_item_repetition_in_array,\
    find_highest_number_in_array, find_min_in_array


# draw 10 letters from the pile randomly
# remove chosen letter from pile
def draw_letters():
    letters_pile = create_a_pile_of_letters()
    hand = []

    for _ in range(HAND_SIZE):
        # find random index
        random_index = random.randint(0, len(letters_pile)-1)
        # swap letter at this random index with the last one in list
        last_letter = letters_pile[-1]
        letters_pile[-1] = letters_pile[random_index]
        letters_pile[random_index] = last_letter
        # add our new last letter to hand and remove it from our list
        hand.append(letters_pile.pop())
    
    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if (count_item_repetition_in_array(letter, word) != 
            count_item_repetition_in_array(letter, letter_bank)):
            return False
    return True

def score_word(word):
    word = word.upper()
    word_score = 0

    for letter in word:
        word_score += SCORE_CHART[letter]

    if 7 <= len(word) <= 10:
        word_score += 8

    return word_score

def get_highest_word_score(word_list):
    # create a list of scores corresponding to the word_list
    scores_list = []

    for word in word_list:
        scores_list.append(score_word(word))

    # find the highest score in scores_list
    highest_score = find_highest_number_in_array(scores_list)

    # make a list that contains only words with highest score
    # make a corresponding list that contains len() of these words
    highest_score_words = []
    highest_score_words_len = []

    for index in range(len(scores_list)):
        if scores_list[index] == highest_score:
            highest_score_words.append(word_list[index])
            highest_score_words_len.append(len(word_list[index]))
    
    # set logic for choosing winning word 
    # from the list of words with highest scores
    if len(highest_score_words) == 1:
        win_word = highest_score_words[0]
    else:
        if 10 in highest_score_words_len:
            win_word = highest_score_words[highest_score_words_len.index(10)]
        else:
            win_word_len = find_min_in_array(highest_score_words_len)
            win_word_index = highest_score_words_len.index(win_word_len)
            win_word = highest_score_words[win_word_index]

    return win_word, highest_score