from constants import LETTER_POOL


# creates a pile of all available letters (list)
# for correct distribution probability purposes
def create_a_pile_of_letters():
    pile_of_unpacked_letters = []

    for letter, number in LETTER_POOL.items():
        pile_of_unpacked_letters.extend(letter * number)
    
    return pile_of_unpacked_letters

# counts how many times item appears in array
def count_item_repetition_in_array(item_to_count, array):
    count = 0
    for item in array:
        if item == item_to_count:
            count += 1
    return count

# finds highest number in array of numbers
def find_highest_number_in_array(array):
    highest_number = 0
    for number in array:
        if number > highest_number:
            highest_number = number
    return highest_number

# finds minimum number in array    
def find_min_in_array(array):
    min_value = array[0]
    for value in array:
        if value < min_value:
            min_value = value
    return min_value