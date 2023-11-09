import re

elfPositions = set([(idx, m.start()) for idx, line in enumerate(open('input.txt').read().split('\n')) for m in re.finditer('#', line)])

directions = [
    ((-1, 0),   ((-1, 0), (-1, -1), (-1, 1))),
    ((1, 0),    ((1, 0), (1, -1), (1, 1))),
    ((0, -1),   ((0, -1), (-1, -1), (1, -1))),
    ((0, 1),    ((0, 1), (-1, 1), (1, 1))),
]

def makeMove(positions, directionIdxStart):
    prevPositions = dict()
    nextPositions = dict()
    for pos in positions:
        nextPos = pos

        needMove = False        
        for d0, d1 in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (pos[0] + d0, pos[1] + d1) in positions:
                needMove = True
                break

        if needMove:
            for directionIdx in range(4):
                available = True
                direction = directions[(directionIdxStart + directionIdx) % 4]

                for adjacentDirection in direction[1]:
                    adjacentPos = (pos[0] + adjacentDirection[0], pos[1] + adjacentDirection[1])
                    if adjacentPos in positions:
                        available = False
                        break
                
                if available:
                    nextPos = (pos[0] + direction[0][0], pos[1] + direction[0][1])
                    break
        
        if nextPos in prevPositions:
            nextPositions[pos] = pos
            nextPositions[prevPositions[nextPos]] = prevPositions[nextPos]
        else:
            prevPositions[nextPos] = pos
            nextPositions[pos] = nextPos
    
    return set(nextPositions.values())

round = 1
directionIdxStart = 0
while True:
    newElfPositions = makeMove(elfPositions, directionIdxStart)
    
    if round == 10:
        rect = (
            min([pos[0] for pos in newElfPositions]),
            min([pos[1] for pos in newElfPositions]),
            max([pos[0] for pos in newElfPositions]),
            max([pos[1] for pos in newElfPositions]),
        )
        print('Part 1: {}'.format((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) - len(newElfPositions)))    # 3966
    
    if newElfPositions == elfPositions:
        print('Part 2: {}'.format(round))                                                                       # 933
        break

    directionIdxStart = (directionIdxStart + 1) % 4
    elfPositions = newElfPositions
    round += 1
    