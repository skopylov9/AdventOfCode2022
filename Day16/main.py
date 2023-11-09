nodesWeight = {}
nodesNeighbors = {}
for line in open('input.txt').read().split('\n'):
    source, targets = line.split('; ')
    nodesWeight[source[6:8]] = int(source[23:])
    nodesNeighbors[source[6:8]] = targets.replace('s', '')[21:].split(', ') + [source[6:8]]

valuebleEdges = sorted([key for key, value in nodesWeight.items() if value > 0])
allEdges = sorted(nodesWeight.keys())

nodesWeightByIndex = [nodesWeight[edge] for edge in allEdges]
nodesNeighborsByIndex = [[allEdges.index(node) for node in nodesNeighbors[edge]] for edge in allEdges]

l1 = 2**len(valuebleEdges)
l2 = len(allEdges)
listOfMatrix = [[[0 for _ in range(l1)] for _ in range(l2)] for _ in range(31)]

def calcBest(matrix2d, matrix2dNew, toErnTime):
    for positionIndex in range(len(matrix2dNew)):
        position = allEdges[positionIndex]

        index = -1
        if position in valuebleEdges:
            index = valuebleEdges.index(position)

        for availableEdges in range(len(matrix2dNew[positionIndex])):
            best = 0
            if index != -1:
                if (1 << index) & availableEdges:
                    bestRate = matrix2d[positionIndex][(~(1 << index)) & availableEdges]
                    bestRate = bestRate + nodesWeightByIndex[positionIndex] * (toErnTime - 1)

                    if bestRate > best:
                        best = bestRate
            for targetNodeIndex in nodesNeighborsByIndex[positionIndex]:
                bestRate = matrix2d[targetNodeIndex][availableEdges]
                if bestRate > best:
                    best = bestRate
            
            matrix2dNew[positionIndex][availableEdges] = best
    return matrix2dNew

for i in range(1, 31):
    calcBest(listOfMatrix[i - 1], listOfMatrix[i], i)
    print('Calculating...')

print('Part 1: {}'.format(listOfMatrix[30][0][l1 - 1]))                                                                 # 2181
print('Part 2: {}'.format(max([listOfMatrix[26][0][i] + listOfMatrix[26][0][(~i) & (l1 - 1)] for i in range(l1 - 1)]))) # 2824
