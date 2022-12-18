import copy

moves = open('input.txt').read()
boardWidth = 7
shapes = []
shapes.append([[1, 1, 1, 1]])
shapes.append([[0, 1, 0],
               [1, 1, 1],
               [0, 1, 0]])
shapes.append([[0, 0, 1],
               [0, 0, 1],
               [1, 1, 1]])
shapes.append([[1],
               [1],
               [1],
               [1]])
shapes.append([[1, 1],
               [1, 1]])

def addRow(boardRow, shapeRow, shapeY):
    for y in range(len(shapeRow)):
        boardRow[y + shapeY] += shapeRow[y]
    return boardRow

def checkRow(boardRow, shapeRow, shapeY):
    for y in range(len(shapeRow)):
        if boardRow[y + shapeY] + shapeRow[y] > 1:
            return False
    return True

def checkShape(board, shape, shapeX, shapeY):
    if shapeY not in range(boardWidth - len(shape[0]) + 1) or shapeX < 0:
        return False
    if shapeX >= len(board):
        return True
    for rowIndex in range(len(shape)):
        inboardRow = shapeX + len(shape) - 1 - rowIndex
        if inboardRow < len(board) and not checkRow(board[inboardRow], shape[rowIndex], shapeY):
            return False      
    return True

def addShapeToBorder(board, shape, shapeX, shapeY):
    while shapeX + len(shape) > len(board):
        board.append([0 for _ in range(boardWidth)])
    for rowIndex in range(len(shape)):
        addRow(board[shapeX + len(shape) - 1 - rowIndex], shape[rowIndex], shapeY)

def makeMove(board, shape, moveIndex, shapeX, shapeY):
    move = -1 if moves[moveIndex] == '<' else 1
    return shapeY + move if checkShape(board, shape, shapeX, shapeY + move) else shapeY

def checkBordAfterSomeStones(stoppedCount):
    board = []

    stonesCount = 0
    shapeIndex = 0
    moveIndex = 0

    toAddForCycles = 0
    cycleDetector = dict()
    while stonesCount < stoppedCount:
        stonesCount += 1
        shapeY = 2
        shapeX = len(board) + 3

        if toAddForCycles == 0:
            if (shapeIndex, moveIndex) not in cycleDetector:
                cycleDetector[(shapeIndex, moveIndex)] = []
            cycleDetectorForMove = cycleDetector[(shapeIndex, moveIndex)]
            cycleDetectorForMove.append((stonesCount, len(board)))

            if len(cycleDetectorForMove) > 2:
                cycleSize = cycleDetectorForMove[-1][0] - cycleDetectorForMove[-2][0]
                cycleHeight = cycleDetectorForMove[-1][1] - cycleDetectorForMove[-2][1]

                toAddCycles = (stoppedCount - stonesCount) // cycleSize
                stonesCount += toAddCycles * cycleSize
                toAddForCycles = cycleHeight * toAddCycles

                if stonesCount >= stoppedCount:
                    break

        shape = shapes[shapeIndex]
        shapeIndex = (shapeIndex + 1) % len(shapes)
        while checkShape(board, shape, shapeX, shapeY):
            shapeY = makeMove(board, shape, moveIndex, shapeX, shapeY)
            moveIndex = (moveIndex + 1) % len(moves)
            shapeX -= 1
        
        addShapeToBorder(board, shape, shapeX + 1, shapeY)
    
    return len(board) + toAddForCycles

print('Part 1:', checkBordAfterSomeStones(2022))
print('Part 2:', checkBordAfterSomeStones(1_000_000_000_000))