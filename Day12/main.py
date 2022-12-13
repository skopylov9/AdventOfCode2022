lines = open("input.txt").read().split('\n')

for i in range(len(lines)):
    if 'E' in lines[i]:
        startNode = (i, lines[i].index('E'))
        lines[i] = lines[i].replace('E', 'z')
    if 'S' in lines[i]:
        finishNode = (i, lines[i].index('S'))
        lines[i] = lines[i].replace('S', 'a')

matrix = [[0 for _ in range(len(lines[i]))] for i in range(len(lines))]
toCheckNode = [startNode]

while toCheckNode:
    sourceNode = toCheckNode.pop(0)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        targetNode = (sourceNode[0] + dx, sourceNode[1] + dy)
        if targetNode[0] not in range(len(matrix)) or targetNode[1] not in range(len(matrix[0])):
            continue
        if matrix[targetNode[0]][targetNode[1]] != 0:
            continue
        if ord(lines[sourceNode[0]][sourceNode[1]]) - 1 <= ord(lines[targetNode[0]][targetNode[1]]):
            matrix[targetNode[0]][targetNode[1]] = matrix[sourceNode[0]][sourceNode[1]] + 1
            toCheckNode.append(targetNode)

print(matrix[finishNode[0]][finishNode[1]])
print(min([matrix[i][j] for j in range(len(matrix[i])) for i in range(len(matrix)) if lines[i][j] == 'a' and matrix[i][j] != 0]))
