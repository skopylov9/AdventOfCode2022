import re

sourceData = open('input.txt').read().split('\n')

blizzards = set([({'>':0,'v':1,'<':2,'^':3}[line[m.start()]], (idx - 1, m.start() - 1)) for idx, line in enumerate(sourceData) for m in re.finditer('[>v<\^]', line)])

directions = {
    -1 : (0, 0),
    0  : (0, 1),
    1  : (1, 0),
    2  : (0, -1),
    3  : (-1, 0),
}

def applyOffset(direction, pos):
    return (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

def checkPosValid(pos, lenAxis0, lenAxis1):
    return (pos in [(-1, 0), (lenAxis0, lenAxis1 - 1)]) or ((0 <= pos[0] < lenAxis0) and (0 <= pos[1] < lenAxis1))

def validateBlizzardPos(pos, lenAxis0, lenAxis1):
    return ((pos[0] + lenAxis0) % lenAxis0,
            (pos[1] + lenAxis1) % lenAxis1)
    
def makeBlizzardsMove(blizzards, lenAxis0, lenAxis1):
    newBlizzards = set()
    for blizzard in blizzards:
        newBlizzards.add((blizzard[0], validateBlizzardPos(applyOffset(blizzard[0], blizzard[1]), lenAxis0, lenAxis1)))
    return newBlizzards

def makeExpeditionMove(possiblePositions, blizzards, lenAxis0, lenAxis1):
    newPossiblePositions = set()
    blizzardsPos = set([blizzard[1] for blizzard in blizzards])
    for pos in possiblePositions:
        for direction in [-1, 0, 1, 2, 3]:
            newPos = applyOffset(direction, pos)
            if checkPosValid(newPos, lenAxis0, lenAxis1) and (newPos not in blizzardsPos):
                newPossiblePositions.add(newPos)
    return newPossiblePositions

def searchShortestPath(posFrom, posTo, blizzards, lenAxis0, lenAxis1):
    step = 0
    possiblePositions = set([posFrom])
    while True:
        step += 1
        blizzards = makeBlizzardsMove(blizzards, lenAxis0, lenAxis1)
        possiblePositions = makeExpeditionMove(possiblePositions, blizzards, lenAxis0, lenAxis1)

        if posTo in possiblePositions:
            break

    return step, blizzards

lenAxis0 = len(sourceData) - 2
lenAxis1 = len(sourceData[0]) - 2

stepToEnd, blizzards = searchShortestPath((-1, 0), (lenAxis0, lenAxis1 - 1), blizzards, lenAxis0, lenAxis1)
stepToBegin, blizzards = searchShortestPath((lenAxis0, lenAxis1 - 1), (-1, 0), blizzards, lenAxis0, lenAxis1)
stepToEndAgain, blizzards = searchShortestPath((-1, 0), (lenAxis0, lenAxis1 - 1), blizzards, lenAxis0, lenAxis1)

print('Part 1: {}'.format(stepToEnd))                                   # 297
print('Part 2: {}'.format(stepToEnd + stepToBegin + stepToEndAgain))    # 856