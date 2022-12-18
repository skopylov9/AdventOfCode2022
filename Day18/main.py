cubes = open('input.txt').read().split('\n')
cubes = [tuple([int(point) + 1 for point in cube.split(',')]) for cube in cubes]

# Independent decision of the first part
# lines = dict()
# for cube in cubes:
#     for mx, my, mz in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]:
#         tCube = (cube[0] * mx, cube[1] * my, cube[2] * mz)
#         if tCube not in lines:
#             lines[tCube] = []
#         lines[tCube].append(cube[(mx, my, mz).index(0)])

# count = 0
# for key, value in lines.items():
#     value.sort()
#     for i in range(len(value) - 1):
#         count += 1 if value[i] + 1 == value[i + 1] else 0

# print('Part 1:', len(cubes) * 6 - count * 2)

# Generate 3D matrix for all possible points. Possible values. 0 - air, 1 - lava, 2 - water
maxSize = 0
for cube in cubes:
    maxSize = max(maxSize, max(cube))
maxSize += 2
space = [[[0 for _ in range(maxSize)] for _ in range(maxSize)] for _ in range(maxSize)]

# Applying lava to matrix
for cube in cubes:
    space[cube[0]][cube[1]][cube[2]] = 1

# Apply water to matrix
queue = [(0,0,0)]
while queue:
    point = queue.pop(0)
    for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        nextPoint = (point[0] + dx, point[1] + dy, point[2] + dz)
        if nextPoint[0] in range(maxSize) and nextPoint[1] in range(maxSize) and nextPoint[2] in range(maxSize):
            if space[nextPoint[0]][nextPoint[1]][nextPoint[2]] == 0:
                space[nextPoint[0]][nextPoint[1]][nextPoint[2]] = 2
                queue.append(nextPoint)

part1 = 0
part2 = 0
for i in range(maxSize):
    for j in range(maxSize):
        lines = [[space[i][j][k] for k in range(maxSize)],
                 [space[i][k][j] for k in range(maxSize)],
                 [space[k][i][j] for k in range(maxSize)]]
        for line in lines:
            for index in range(len(line) - 1):
                part1 += 1 if line[index] + line[index + 1] in [1, 3] else 0
                part2 += 1 if line[index] + line[index + 1] == 3 else 0

print('Part 1:', part1)
print('Part 2:', part2)
