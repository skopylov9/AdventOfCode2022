def makeSetFromRange(section):
    return set(range(int(section.split('-')[0]), int(section.split('-')[1]) + 1))

inputLines = open("input.txt").read().split("\n")
sectionPairs = [list(map(makeSetFromRange, inputLine.split(','))) for inputLine in inputLines]

print(sum([1 if (pair[0].issubset(pair[1]) or pair[1].issubset(pair[0])) else 0 for pair in sectionPairs]))
print(sum([1 if len(pair[0] & pair[1]) else 0 for pair in sectionPairs]))
