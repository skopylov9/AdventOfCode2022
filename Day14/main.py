import copy
import bisect

sourceRocks = {}
for path in open('input.txt').read().split('\n'):
    points = path.split(' -> ')
    lines = [(list(map(int, points[i].split(','))), list(map(int, points[i + 1].split(',')))) for i in range(len(points) - 1)]

    for line in lines:
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
            for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                if i not in sourceRocks:
                    sourceRocks[i] = set()
                sourceRocks[i].add(j)

for index, column in sourceRocks.items():
    sourceRocks[index] = sorted(list(column))

def fallSand(bariers, sand):
    if sand[0] not in bariers:
        return (True, False, (0,0))
    
    column = bariers[sand[0]]
    index = bisect.bisect_left(column, sand[1])
    if index == len(column):
        return (True, False, (0,0))

    newPos = column[index]
    if newPos == sand[1]:
        return (False, True, (0,0))

    fall, blocked, next = fallSand(bariers, (sand[0] - 1, newPos))
    if not fall and blocked:
        fall, blocked, next = fallSand(bariers, (sand[0] + 1, newPos))
        if not fall and blocked:
            fall, blocked, next = (False, False, (sand[0], newPos - 1))
    return fall, blocked, next

def simulateSandsForBariers(bariers):
    sandCount = 0
    while True:
        fall, blocked, sand = fallSand(bariers, (500, 0))
        if fall or blocked:
            break

        sandCount += 1
        index = bisect.bisect_left(bariers[sand[0]], sand[1])
        bariers[sand[0]].insert(index, sand[1])
    return sandCount

print('Part 1:', simulateSandsForBariers(copy.deepcopy(sourceRocks)))

floor = max([max(column) for column in sourceRocks.values()]) + 2
for i in range(500 - floor, 500 + floor + 1):
    if i not in sourceRocks:
        sourceRocks[i] = []
    sourceRocks[i].append(floor)
print('Part 2:', simulateSandsForBariers(copy.deepcopy(sourceRocks)))