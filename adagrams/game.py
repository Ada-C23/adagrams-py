from random import randint
letters_pool={"A":9,"B":2,"C":2,"D":4,"E":12,"F":2,"G":3,"H":2,"I":9,"J":1,"K":1,"L":4,"M":2,"N":6,"O":8,"P":2,"Q":1,"R":6,"S":4,"T":6,"U":4,"V":2,"W":2,"X":1,"Y":2,"Z":1}
def draw_letters():
    drawed_letters=[]
    all_letters=[]
    letters_pool={"A":9,"B":2,"C":2,"D":4,"E":12,"F":2,"G":3,"H":2,"I":9,"J":1,"K":1,"L":4,"M":2,"N":6,"O":8,"P":2,"Q":1,"R":6,"S":4,"T":6,"U":4,"V":2,"W":2,"X":1,"Y":2,"Z":1}
    for letter, quantity in letters_pool.items():
        for i in range(quantity):
            all_letters.append(letter)
    while len(drawed_letters)<10:
        random_number= randint(0,len(all_letters)-1) 
        drawn_letter=all_letters[random_number]
        drawed_letters.append(drawn_letter)
        all_letters.pop(random_number)
        letters_pool[drawn_letter] -= 1
    return drawed_letters

def uses_available_letters(word, letter_bank):
    letter_bank_count={}
    word_count={}
    word=word.upper()
    for letter in letter_bank:
        if letter not in letter_bank_count:
            letter_bank_count[letter]=1
        else:
            letter_bank_count[letter]+=1

    for letter in word:
        if letter not in word_count:
            word_count[letter]=1
        else:
            word_count[letter]+=1
    for letter in word: 
        if letter not in letter_bank or word_count[letter]>letter_bank_count[letter]:
            return False
 #   all checks passed then return True
    return True

#score_chart={['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:1,['D','G']:2,['B','C','M','P']:3,['F','H','V','W','Y']:4,['K']:5,['J','X']:8,['Q','Z']:10}
score_chart={1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
             2:["D","G"],3:["B","C","M","P"],
             4:["F","H","V","W","Y"],5:["K"],
             8:["J","X"],10:["Q","Z"]}
def score_word(word):
    flatten_score_chart={}
    total_score=0
    word=word.upper()
    for score, letters in score_chart.items():
        for letter in letters:
            flatten_score_chart[letter]=score
    for letter in word:
        total_score+=flatten_score_chart[letter]
    if len(word)>=7 and len(word)<=10:
        total_score+=8
    return total_score


def get_highest_word_score(word_list):

    max_score=0
    highest_score={}
    
    for word in word_list:
        score = score_word(word)
        highest_score[word]=score
        if score > max_score:
            max_score = score
            highest_score_word = word
        elif score == max_score:
            if len(word) == 10 and len(highest_score_word)!=10:
                highest_score_word=word
            elif len(word) < len(highest_score_word) and len(highest_score_word)!=10:
                highest_score_word=word
            else:
                continue
    final_score=(highest_score_word, max_score)

    return final_score


