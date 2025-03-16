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
def uses_available_letters(word, letter_bank):
    word_list = list(word)
    correct_list = []
    for i in word_list:
        if i in letter_bank:
            correct_list.append(i)
            letter_bank.remove(i)
        else:
            return False
    return correct_list == word_list

letter_bank = ['A', 'P', 'L', 'E']
print(uses_available_letters("EEEE", letter_bank))
