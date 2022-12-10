def findSameElement(listOfElementsList):
    return next(iter(set.intersection(*map(set, listOfElementsList))))

def calcPrio(types):
    return sum([ord(type) - (96 if type.islower() else 38) for type in types])

def makeTwoParts(iterable):
    return [iterable[:len(iterable) // 2], iterable[len(iterable) // 2:]]

rucksacks = open("input.txt").read().split("\n")

sameElementInCompartments = [findSameElement(makeTwoParts(rucksack)) for rucksack in rucksacks]
sameElementInGroups = [findSameElement(rucksacks[i : i + 3]) for i in range(0, len(rucksacks), 3)]

print(calcPrio(sameElementInCompartments))
print(calcPrio(sameElementInGroups))
