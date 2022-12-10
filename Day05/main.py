stacksInput, movesInput = open("input.txt").read().split("\n\n")

matrix = stacksInput.split('\n')
new_matrix = [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]))]
stacksList = [''.join(line).strip() for line in new_matrix if line[0].isnumeric()]

moves = [move.replace('move ', '').replace('from ', '').replace('to ', '') for move in movesInput.split('\n')]
moves = [[int(v) for v in move.split(' ')] for move in moves]

stacksList1 = stacksList[::]
for move in moves:
    stacksList1[move[2] - 1] += stacksList1[move[1] - 1][-move[0]::][::-1]
    stacksList1[move[1] - 1] = stacksList1[move[1] - 1][:-move[0]:]
print(''.join([column[-1] for column in stacksList1]))

stacksList2 = stacksList[::]
for move in moves:
    stacksList2[move[2] - 1] += stacksList2[move[1] - 1][-move[0]::]
    stacksList2[move[1] - 1] = stacksList2[move[1] - 1][:-move[0]:]
print(''.join([column[-1] for column in stacksList2]))
