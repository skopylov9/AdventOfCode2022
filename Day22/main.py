matrix, road = open('input.txt').read().split('\n\n')
maxlen = max([len(line) for line in matrix.split('\n')])
matrix = [line.ljust(maxlen, ' ') for line in matrix.split('\n')]

sourceMatrix = matrix
matrix = [' ' + line + ' ' for line in [' ' * maxlen] + matrix + [' ' * maxlen]]
matrix = [line.replace(' ', '*') for line in matrix]
rotatedMatrix = [''.join(line[::-1]) for line in zip(*matrix[::-1])]

cubeFaceSize = 50

packedMatrix = sourceMatrix
packedMatrix = [''.join([' ' if face == " " * cubeFaceSize else '#' for face in (line[idx : idx + cubeFaceSize] for idx in range(0, len(line), cubeFaceSize))]) for line in packedMatrix]
packedMatrix = [''.join(line[::-1]) for line in zip(*packedMatrix[::-1])]
packedMatrix = [''.join([' ' if face == " " * cubeFaceSize else '#' for face in (line[idx : idx + cubeFaceSize] for idx in range(0, len(line), cubeFaceSize))]) for line in packedMatrix]
packedMatrix = [''.join(line[::-1]) for line in zip(*packedMatrix[::-1])]
packedMatrix = [''.join(line[::-1]) for line in zip(*packedMatrix[::-1])]
packedMatrix = [''.join(line[::-1]) for line in zip(*packedMatrix[::-1])]

orMap = {0 : (0, 1), 1 : (1, 0), 2 : (0, -1), 3 : (-1, 0)}

faceRelations = {
    (1, 0) : (6, 0), (1, 1) : (2, 1), (1, 2) : (5, 2), (1, 3) : (4, 3),
    (2, 0) : (6, 3), (2, 1) : (3, 1), (2, 2) : (5, 3), (2, 3) : (1, 3),
    (3, 0) : (6, 2), (3, 1) : (4, 1), (3, 2) : (5, 0), (3, 3) : (2, 3),
    (4, 0) : (6, 1), (4, 1) : (1, 1), (4, 2) : (5, 1), (4, 3) : (3, 3),
    (5, 0) : (1, 0), (5, 1) : (2, 0), (5, 2) : (3, 0), (5, 3) : (4, 0),
    (6, 0) : (3, 2), (6, 1) : (2, 2), (6, 2) : (1, 2), (6, 3) : (4, 2),
}

indexToPos = {}
def fixRelation(pos, index):
    packedMatrix[pos[0] - 1] = packedMatrix[pos[0] - 1][:pos[1] - 1] + str(index) + packedMatrix[pos[0] - 1][pos[1]:]
    indexToPos[index] = (pos[0] - 1, pos[1] - 1)
    for orient, offset in orMap.items():
        newPos = (pos[0] + offset[0], pos[1] + offset[1])
        if (newPos[0] - 1) not in range(len(packedMatrix)) or (newPos[1] - 1) not in range(len(packedMatrix[newPos[0] - 1])) or packedMatrix[newPos[0] - 1][newPos[1] - 1] != '#':
            continue

        newIndex, newOrient = faceRelations[(index, orient)]
        if newOrient != orient:
            faceRelationsCopy = faceRelations.copy()
            for orient2 in orMap:
                rel = faceRelationsCopy[(newIndex, (orient2 + 4 + (newOrient - orient)) % 4)]
                faceRelations[(newIndex, orient2)] = faceRelationsCopy[(newIndex, (orient2 + 4 + (newOrient - orient)) % 4)]
                faceRelations[(rel[0], (rel[1] + 2) % 4)] = (newIndex, (orient2 + 2) % 4)
        fixRelation(newPos, newIndex)
fixRelation((1, packedMatrix[0].index('#') + 1), 1)

def calcBorderPath(faceNum, orient):
    nextFace, nextOrient = faceRelations[(faceNum, orient)]
    nextFacePos = indexToPos[nextFace]
    nextFacePos = (nextFacePos[0] * cubeFaceSize, nextFacePos[1] * cubeFaceSize)
    if 0 == nextOrient or 2 == nextOrient:
        if (orient in [0, 3] and nextOrient == 0) or (orient in [1, 2] and nextOrient == 2):
            nextFacePos = (nextFacePos[0] + (idx - 1) % cubeFaceSize + 1, nextFacePos[1] + (cubeFaceSize if 2 == nextOrient else 1))
        else:
            nextFacePos = (nextFacePos[0] + cubeFaceSize - (idx - 1) % cubeFaceSize, nextFacePos[1] + (cubeFaceSize if 2 == nextOrient else 1))
    else:
        if (orient in [0, 3] and nextOrient == 1) or (orient in [1, 2] and nextOrient == 3):
            nextFacePos = (nextFacePos[0] + (cubeFaceSize if 3 == nextOrient else 1), nextFacePos[1] + cubeFaceSize - (idx - 1) % cubeFaceSize)
        else:
            nextFacePos = (nextFacePos[0] + (cubeFaceSize if 3 == nextOrient else 1), nextFacePos[1] + (idx - 1) % cubeFaceSize + 1)
    
    if orient == 2:
        borderTransformTask2[(orient, (idx, start - 1))] = (nextOrient, nextFacePos)
    elif orient == 0:
        borderTransformTask2[(orient, (idx, end + 1))] = (nextOrient, nextFacePos)
    elif orient == 3:
        borderTransformTask2[(orient, (start - 1, idx))] = (nextOrient, nextFacePos)
    elif orient == 1:
        borderTransformTask2[(orient, (end + 1, idx))] = (nextOrient, nextFacePos)

borderTransformTask2 = {}
for idx, line in enumerate(matrix):
    if '.' not in line and '#' not in line:
        continue
    start = (line.index('*.') if '*.' in line else line.index('*#')) + 1
    end = (line.index('.*') if '.*' in line else line.index('#*'))

    calcBorderPath(int(packedMatrix[(idx - 1) // cubeFaceSize][(end - 1) // cubeFaceSize]), 0)
    calcBorderPath(int(packedMatrix[(idx - 1) // cubeFaceSize][(start - 1) // cubeFaceSize]), 2)

for idx, line in enumerate(rotatedMatrix):
    if '.' not in line and '#' not in line:
        continue
    start = (line.index('*.') if '*.' in line else line.index('*#')) + 1
    end = (line.index('.*') if '.*' in line else line.index('#*'))

    calcBorderPath(int(packedMatrix[(start - 1) // cubeFaceSize][(idx - 1) // cubeFaceSize]), 3)
    calcBorderPath(int(packedMatrix[(end - 1) // cubeFaceSize][(idx - 1) // cubeFaceSize]), 1)

# _________
# |###|516|
# | # | 2 |
# | # | 3 |
# | # | 4 |
# ---------

# orient : >,      v,      <,      ^
# face 1 : (6, >), (2, v), (5, <), (4, ^)
# face 2 : (6, ^), (3, v), (5, ^), (1, ^)
# face 3 : (6, <), (4, v), (5, >), (2, ^)
# face 4 : (6, v), (1, v), (5, v), (3, ^)
# face 5 : (1, >), (2, >), (3, >), (4, >)
# face 6 : (3, <), (2, <), (1, <), (4, <)

# ____________________
# | ##| 16||  # |  1 |
# | # | 2 ||### |452 |
# |## |53 ||  ##|  36|
# |#  |4  ||    |    |
# --------------------

borderTransform = {}
for idx, line in enumerate(matrix):
    if '.' not in line and '#' not in line:
        continue
    start = (line.index('*.') if '*.' in line else line.index('*#')) + 1
    end = (line.index('.*') if '.*' in line else line.index('#*'))
    borderTransform[(2, (idx, start - 1))] = (2, (idx, end))
    borderTransform[(0, (idx, end + 1))] = (0, (idx, start))

for idx, line in enumerate(rotatedMatrix):
    if '.' not in line and '#' not in line:
        continue
    start = (line.index('*.') if '*.' in line else line.index('*#')) + 1
    end = (line.index('.*') if '.*' in line else line.index('#*'))
    borderTransform[(3, (start - 1, idx))] = (3, (end, idx))
    borderTransform[(1, (end + 1, idx))] = (1, (start, idx))

def makeAction(action, orient, pos, borderTransform):
    if action == 'R':
        return (orient + 1) % 4, pos
    if action == 'L':
        return (orient + 3) % 4, pos
    
    for _ in range(int(action)):
        newPos = (pos[0] + orMap[orient][0], pos[1] + orMap[orient][1])
        newOrient = orient
        if matrix[newPos[0]][newPos[1]] == '*':
            newOrient, newPos = borderTransform[(orient, newPos)]
        if matrix[newPos[0]][newPos[1]] == '#':
            break
        pos = newPos
        orient = newOrient
    return orient, pos

posTask2 = posTask1 = (1, matrix[1].index('*.') + 1)
orientTask2 = orientTask1 = 0

for action in road.replace('R', ' R ').replace('L', ' L ').split(' '):
    orientTask1, posTask1 = makeAction(action, orientTask1, posTask1, borderTransform)
    orientTask2, posTask2 = makeAction(action, orientTask2, posTask2, borderTransformTask2)

print('Part 1: {}'.format(posTask1[0] * 1000 + posTask1[1] * 4 + orientTask1))  # 126350
print('Part 2: {}'.format(posTask2[0] * 1000 + posTask2[1] * 4 + orientTask2))  # 129339
