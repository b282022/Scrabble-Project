import numpy as np
from cross_checks import cross_checks
from utility import common_letters, word_after_anchor, calculate_score, binary_search
from utility import read_dictionary, is_whole_permutation_valid
from anchor import get_anchor_positions
from itertools import permutations

def generate_move_row(board, row, rack, dictionary):
    anchor_positions = get_anchor_positions(board, row)
    allowed_letters = cross_checks(board, row, dictionary) 
    # print allowed_letters
    for i in range(len(allowed_letters)):
        allowed_letters[i] = common_letters(allowed_letters[i], rack)
    if len(anchor_positions) == 0:
        print "No anchors for row:", row
        return (-1, '')
    max_anchor_position = anchor_positions[0] 
    max_left_word = ''
    max_right_word = ''
    max_existing_word = ''
    max_score = -1
    for anchor in anchor_positions:
        # Extending on blank spots to the left of the anchor and anchor itself
        existing_word = word_after_anchor(board, row, anchor)
        print "Existing", existing_word
        max_possible_right_length = 0
        for j in range(anchor + len(existing_word) + 1, len(board)):
            if j != (len(board) - 1):
                if board[row][j + 1] != '-':
                    break
            max_possible_right_length += 1
        print "Right Extension Possible", max_possible_right_length
        for i in range(anchor, anchor - len(rack) -1, -1):
            if i < 0:
                break
            if i != 0:
                if board[row][i - 1] != '-':
                    break
            left_length = anchor - i + 1
            left_permutations_of_rack = list(permutations(rack, left_length))
            # print "Permutations of Left Length", left_length, left_permutations_of_rack
            for left_permutation in left_permutations_of_rack:
                # Generate all right permutations as well
                remaining_rack = []
                for i in rack:
                    if i not in left_permutation:
                        remaining_rack.append(i)
                left_word = "".join(left_permutation)
                for j in range(0, max_possible_right_length):
                    right_permutations_of_j_length = list(permutations(remaining_rack, j))
                    for right_permutation in right_permutations_of_j_length:
                        right_word = "".join(right_permutation)
                        if is_whole_permutation_valid(left_word, existing_word, right_word, allowed_letters, anchor, dictionary) == False:
                            continue
                        whole_word = left_word + existing_word + right_word
                        score = calculate_score(whole_word)
                        if score > max_score:
                            max_score = score
                            max_anchor_position = anchor
                            max_left_word = left_word
                            max_existing_word = existing_word
                            max_right_word = right_word
    return (max_anchor_position, max_left_word, max_existing_word, max_right_word)


def generate_move_for_all_rows(board, rack, dictionary):
    print board
    all_moves_rows = []
    for row in range(len(board)):
        best_move_for_row = generate_move_row(board, row, rack, dictionary)
        all_moves_rows.append(best_move_for_row)
        print "Best move for row", row, "is", best_move_for_row
    return all_moves_rows


def generate_all_moves(board, rack, dictionary):
    all_moves = []
    print "Moves for all the rows"
    all_moves.append(generate_move_for_all_rows(board, rack, dictionary))
    print "Moves for all the columns"
    board_transpose = np.transpose(board)
    all_moves.append(generate_move_for_all_rows(board_transpose, rack, dictionary))
    return all_moves


if __name__ == '__main__':
    dictionary = read_dictionary()
    board = np.array([
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 'c', 'a', 'r', 't', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 'r', '-', 'a', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 'o', '-', 'r', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 'r', '-', 'e', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 'e', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', 's', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    ])
    rack = ['w', 'e', 'c', 'l', 'o', 'm', 's']
    all_moves = generate_all_moves(board, rack, dictionary)
    # print best_move_for_row(all_moves[0])
    # print best_move_for_col(all_moves[1])