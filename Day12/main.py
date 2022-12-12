import copy
from functools import reduce

lines = open("input.txt").read().split('\n')

for i in range(len(lines)):
    if 'E' in lines[i]:
        startNode = (i, lines[i].index('E'))
        lines[i] = lines[i].replace('E', 'z')
    if 'S' in lines[i]:
        finishNode = (i, lines[i].index('S'))
        lines[i] = lines[i].replace('S', 'a')

matrix = [[0 for j in range(len(lines[i]))] for i in range(len(lines))]
toCheckNode = [(startNode[0], startNode[1], 0)]

def validateAndAdd(sourceNode, targetNode):
    if targetNode[0] < 0 or targetNode[0] >= len(matrix):
        return
    if targetNode[1] < 0 or targetNode[1] >= len(matrix[0]):
        return
    if matrix[targetNode[0]][targetNode[1]] <= targetNode[2] and matrix[targetNode[0]][targetNode[1]] != 0:
        return
    if ord(lines[sourceNode[0]][sourceNode[1]]) - 1 <= ord(lines[targetNode[0]][targetNode[1]]):
        matrix[targetNode[0]][targetNode[1]] = targetNode[2]
        toCheckNode.append(targetNode)

while toCheckNode:
    index = min(range(len(toCheckNode)), key=lambda i: toCheckNode[i][2])
    sourceNode = toCheckNode[index]
    toCheckNode = toCheckNode[:index] + toCheckNode[index + 1:]

    validateAndAdd(sourceNode, (sourceNode[0] + 1, sourceNode[1], sourceNode[2] + 1))
    validateAndAdd(sourceNode, (sourceNode[0] - 1, sourceNode[1], sourceNode[2] + 1))
    validateAndAdd(sourceNode, (sourceNode[0], sourceNode[1] + 1, sourceNode[2] + 1))
    validateAndAdd(sourceNode, (sourceNode[0], sourceNode[1] - 1, sourceNode[2] + 1))

print(matrix[finishNode[0]][finishNode[1]])
print(min([matrix[i][j] for j in range(len(matrix[i])) for i in range(len(matrix)) if lines[i][j] == 'a' and matrix[i][j] != 0]))
