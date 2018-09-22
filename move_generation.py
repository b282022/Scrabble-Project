from cross_checks import cross_checks
from utility import common_letters, word_after_anchor, calculate_score, binary_search
from utility import read_dictionary
from anchor import get_anchor_positions
from itertools import permutations

def generate_move_row(board, row, rack, dictionary):
    anchor_positions = get_anchor_positions(board, row)
    allowed_letters = cross_checks(board, row, dictionary) 
    # print allowed_letters
    for i in range(len(allowed_letters)):
        allowed_letters[i] = common_letters(allowed_letters[i], rack)
    if len(anchor_positions) == 0:
        print "No anchors for", row
        return (-1, '')
    max_anchor_position = anchor_positions[0] 
    max_left_word = ''
    max_score = -1
    for anchor in anchor_positions:
        # Extending on blank spots to the left of the anchor and anchor itself
        existing_word = word_after_anchor(board, row, anchor)
        print "Existing", existing_word
        for i in range(anchor, anchor - len(rack) -1, -1):
            if i < 0:
                break
            if i != 0:
                if board[row][i - 1] != '-':
                    break
            length = anchor - i + 1
            permutations_of_rack = list(permutations(rack, length))
            # print "Permutations of length", length, permutations_of_rack
            for permutation in permutations_of_rack:
                valid_permutation = True
                for position in range(len(permutation) - 1, -1 , -1):
                    # Last index of permutation matches with anchor
                    if permutation[position] not in allowed_letters[anchor - length + position + 1]:
                        valid_permutation = False
                        break
                if valid_permutation:
                    left_word = "".join(permutation)
                    new_word = left_word + existing_word
                    if binary_search(dictionary, new_word) == -1:
                        continue
                    score = calculate_score(new_word)
                    if score > max_score:
                        max_score = score
                        max_anchor_position = anchor
                        max_left_word = left_word
    return (max_anchor_position, max_left_word)

if __name__ == '__main__':
    dictionary = read_dictionary()
    board = [
        ['-', '-', '-', '-', '-'],
        ['-', 'c', 'a', 'r', '-'],
        ['-', '-', '-', 'e', 't'],
        ['-', '-', '-', 's', '-'],
        ['-', '-', '-', 't', '-'],
    ]
    rack = ['i', 'm', 'a', 'b', 'c', 'r', 'f']
    for row in range(len(board)):
        print generate_move_row(board, row, rack, dictionary)