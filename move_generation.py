from cross_checks import cross_checks
from utility import common_letters, word_after_anchor, calculate_score, binary_search
from utility import read_dictionary
from anchor import get_anchor_positions

def generate_move_row(board, row, rack, dictionary):
    anchor_positions = get_anchor_positions(board, row)
    allowed_letters = cross_checks(board, row, dictionary) 
    print allowed_letters
    for i in range(len(allowed_letters)):
        allowed_letters[i] = common_letters(allowed_letters[i], rack)
    max_anchor_position = anchor_positions[0] 
    letter_chosen = ''
    max_score = -1
    for anchor in anchor_positions:
        # Without extending left or right
        existing_word = word_after_anchor(board, row, anchor)
        print "Existing", existing_word
        for allowed_letter in allowed_letters[anchor]:
            new_word = allowed_letter + existing_word
            if binary_search(dictionary, new_word) == -1:
                continue
            if calculate_score(new_word) > max_score:
                max_score = calculate_score(new_word)
                max_anchor_position = anchor
                letter_chosen = allowed_letter
    return (max_anchor_position, letter_chosen)

if __name__ == '__main__':
    dictionary = read_dictionary()
    print dictionary
    board = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', 'a', 'r', 't'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
    ]
    rack = ['z', 'z', 'z', 'x', 'z', 'z', 'z']
    print generate_move_row(board, 2, rack, dictionary)