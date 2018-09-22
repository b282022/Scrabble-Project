from utility import find_word_above, find_word_below, common_letters, all_letters, read_dictionary


def cross_checks_below(board, row, dictionary):
    valid_letters_below = [[] for _ in range(len(board[row]))]
    for col in range(len(board[row])):
        if board[row][col] != '-':
            continue
        word_below = find_word_below(board, row, col)
        if word_below == '':
            valid_letters_below[col] = all_letters()
        else:
            for word in dictionary:
                if word[1:] == word_below \
                    and word[0] not in valid_letters_below[col]:
                    valid_letters_below[col].append(word[0])
    return valid_letters_below
    

def cross_checks_above(board, row, dictionary):
    valid_letters_above = [[] for _ in range(len(board[row]))]
    for col in range(len(board[row])):
        if board[row][col] != '-':
            continue
        word_above = find_word_above(board, row, col)
        if word_above == '':
            valid_letters_above[col] = all_letters()
        else: 
            for word in dictionary:
                if word.startswith(word_above) \
                and len(word) == len(word_above) + 1 \
                and word[-1] not in valid_letters_above[col]:
                    valid_letters_above[col].append(word[-1])
    return valid_letters_above


def cross_checks(board, row, dictionary):
    if row == 0:
        return cross_checks_below(board, row, dictionary)
    if row == len(board) - 1:
        return cross_checks_above(board, row, dictionary)
    valid_letters_below = cross_checks_below(board, row, dictionary)
    valid_letters_above = cross_checks_above(board, row, dictionary)
    return [common_letters(valid_letters_above[i], valid_letters_below[i]) \
        for i in range(len(valid_letters_above))]


if __name__ == '__main__':
    board = [
        ['-', '-', 'a', '-', '-'],
        ['-', '-', 't', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', 'a', 'z', 't'],
        ['-', '-', 'r', 'z', '-'],
        ['-', '-', 't', '-', '-']
    ]
    print cross_checks(board, 2, read_dictionary())[2]