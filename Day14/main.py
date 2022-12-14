import copy
import bisect

rocks = {}
for path in open('input.txt').read().split('\n'):
    points = path.split(' -> ')
    # lines = [(int(points[i]), int(points[i + 1])) for i in range(len(points) - 1)]
    lines = [(list(map(int, points[i].split(','))), list(map(int, points[i + 1].split(',')))) for i in range(len(points) - 1)]

    for line in lines:
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
            for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                if i not in rocks:
                    rocks[i] = set()
                rocks[i].add(j)



floor = max([max(column) for column in rocks.values()]) + 2

for line in [((500 - floor * 2, floor), (500 + floor * 2, floor))]:
    for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
        for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
            if i not in rocks:
                rocks[i] = set()
            rocks[i].add(j)

for index, column in rocks.items():
    rocks[index] = sorted(list(column))

bariers = copy.deepcopy(rocks)

def ttt(sand):
    if sand[0] not in bariers:
        return (True, False, (0,0))
    
    column = bariers[sand[0]]
    index = bisect.bisect_left(column, sand[1])
    if index == len(column):
        return (True, False, (0,0))

    newPos = column[index]
    if newPos == sand[1]:
        return (False, True, (0,0))

    fall, blocked, left = ttt((sand[0] - 1, newPos))
    if fall:
        return (fall, blocked, left)
    elif not blocked:
        return (fall, blocked, left)

    fall, blocked, right = ttt((sand[0] + 1, newPos))
    if fall:
        return (fall, blocked, right)
    elif not blocked:
        return (fall, blocked, right)

    return (False, False, (sand[0], newPos - 1))




i = 0
while True:
    fall, blocked, sand = ttt((500, 0))
    if fall or blocked:
        break

    i += 1
    index = bisect.bisect_left(bariers[sand[0]], sand[1])
    # bariers[sand[0]] = sorted(bariers[sand[0]] + [sand[1]])
    bariers[sand[0]].insert(index, sand[1])

print(i)