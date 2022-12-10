forest = [[int(treeHight) for treeHight in line] for line in open("input.txt").read().split('\n')]

def checkRange(forest, i, j, rrange, byLine):
    visibleCount = 0
    for r in rrange:
        visibleCount += 1
        if forest[r if byLine else i][r if not byLine else j] >= forest[i][j]:
            return False, visibleCount
    return True, visibleCount

visibleCount = 0
maxSquare = 0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        isVisible1, visibleCount1 = checkRange(forest, i, j, range(i - 1, -1, -1), True)
        isVisible2, visibleCount2 = checkRange(forest, i, j, range(i + 1, len(forest)), True)
        isVisible3, visibleCount3 = checkRange(forest, i, j, range(j - 1, -1, -1), False)
        isVisible4, visibleCount4 = checkRange(forest, i, j, range(j + 1, len(forest[i])), False)

        maxSquare = max(maxSquare, visibleCount1 * visibleCount2 * visibleCount3 * visibleCount4)
        visibleCount += 1 if isVisible1 or isVisible2 or isVisible3 or isVisible4 else 0

print(visibleCount, maxSquare)
