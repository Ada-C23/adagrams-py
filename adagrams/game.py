from random import randint


def draw_letters():
    #copy letter_pool from test and change it from dic to list
    #new variable
    letter_pool = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D',
 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G',
 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L',
 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P',
 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T',
 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

    drawn_letters = []
    #using the row with only from 10 letters that in the letterpool
    for i in range(10):
        if len(letter_pool) == 0:
           break

        index = randint(0, len(letter_pool) - 1)  
        drawn_letters.append(letter_pool[index])  
        letter_pool.pop(index)  

    return drawn_letters 

def uses_available_letters(word, letter_bank):
    #create 2 new variables
   
    letters_bank_copy = list(letter_bank)
    word = word.upper()
    for letter in word:
        if letter not in letters_bank_copy:
          return False
        letters_bank_copy.remove(letter)
    return True

def score_word(word):
    #copy score chart from test
    #create 2 new variables
    Score_chart = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    word = word.upper()  
    total_score = 0  

#count the word's score
    
    for letter in word:  
        if letter in Score_chart:  
            total_score += Score_chart[letter] 
        else:
            total_score += 0  
#arranged an extra bonus           

    if len(word) >= 7 and len(word) <= 10:
        total_score += 8  

    return total_score 


def get_highest_word_score(word_list):
    #create 2 new variables

    best_word = ""
    best_score = 0
#geting score for new word from score_word
#comparing this score with othe word
    for word in word_list:
        score = score_word(word)
        if score > best_score:
            best_word = word
            best_score = score
#cheking if tie have the same score
#If one word has 10 letters and another don't it's winner
        if score == best_score:
           if len(word) == 10:
             if len(best_word) != 10:
              best_word = word
              best_score = score
#if all words not 10 letters lenght count the smaller word as winner
    
           if len(word) != 10 and len(best_word) != 10:
              if len(word) < len(best_word):
               best_word = word
               best_score = score

    return(best_word, best_score)  

    

        

        
