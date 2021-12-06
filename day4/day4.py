
# day 4 - Giant Squid

# -------------------------------------------------------------------- #

# part 1
# Bingo boards and number sequence to mark the numers in the boards in the specific order.
# objective : Start by finding the sum of all unmarked numbers on that board.
# Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
# To guarantee victory against the giant squid, figure out which board will win first. 
# What will your final score be if you choose that board?

with open('input.txt') as f:
    data = [i for i in f.readlines()]
    f.close()

nums = list(int(i) for i in data[0].strip().split(','))
boards = []
solved_boards = []

for i in range(1, len(data)):
    if data[i] == '\n':
        boards.append([])
    else:
        boards[-1].append(list([int(x) for x in data[i].strip().split(' ') if x.isnumeric()]))


def solved(arr, key):
    for i in range(len(arr)):
        if arr[i] == [key for _ in range(len(arr))]:
            return True
        else:
            row_count = 0
            for j in range(len(arr[0])):
                if arr[j][i] == key:
                    row_count += 1

            if row_count == len(arr):
                return True

    return False

def result(board, num):
    total = 0
    for row in board:
        total += sum(row)

    return total * num

def win_solution(boards_, nums_, key_):
    for num in nums_:
        for board in boards_:
            for row in board:
                if num in row:
                    row[row.index(num)] = key_
                    if solved(board, key_):
                        return result(board, num)

# -------------------------------------------------------------------- #

# part 2
# Figure out which board will win last.
# Figure out which board will win last. Once it wins, what would its final score be?

def loss_solution(boards_, nums_, key_):
    solved_indices = []
    for num in nums_:
        for board in boards_:
            for row in board:
                if num in row:
                    row[row.index(num)] = key_
                    if solved(board, key_) and (boards_.index(board) not in solved_indices):
                        solved_boards.append(board)
                        solved_indices.append(boards_.index(board)) 

                    if len(solved_boards) == len(boards):
                        return result(solved_boards[-1], num)  

score1 = win_solution(boards, nums, 0)
score2 = loss_solution(boards, nums, 0)
print(f'score1: {score1}')
print(f'score2: {score2}')

# -------------------------------------------------------------------- #