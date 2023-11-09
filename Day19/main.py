from functools import reduce
from operator import mul

oreRobotCost = 0
clayRobotCost = 0
obsRobotOreCost = 0
obsRobotClayCost = 0
geodeRobotOreCost = 0
geodeRobotObsCost = 0

def deepSearch(rOre, rClay, rObs, rGeod, ore, clay, obs, geod, days, balance, best):
    if days <= 0:
        return geod + balance * days
    
    if geod + (days * (days + 1) // 2) + days * rGeod <= best:
        return 0

    if rObs:
        dayNeed = max(1, ((max(0, geodeRobotOreCost - ore) + rOre - 1) // rOre + 1), ((max(0, geodeRobotObsCost - obs) + rObs - 1) // rObs + 1))
        best = max(best, deepSearch(rOre, rClay, rObs, rGeod + 1,
                                      ore + rOre * dayNeed - geodeRobotOreCost, clay + rClay * dayNeed, obs + rObs * dayNeed - geodeRobotObsCost, geod + rGeod * dayNeed,
                                      days - dayNeed, rGeod, best))

    if rClay and rObs <= geodeRobotObsCost:
        dayNeed = max(1, ((max(0, obsRobotOreCost - ore) + rOre - 1) // rOre + 1), ((max(0, obsRobotClayCost - clay) + rClay - 1) // rClay + 1))
        best = max(best, deepSearch(rOre, rClay, rObs + 1, rGeod,
                                      ore + rOre * dayNeed - obsRobotOreCost, clay + rClay * dayNeed - obsRobotClayCost, obs + rObs * dayNeed, geod + rGeod * dayNeed,
                                      days - dayNeed, rGeod, best))
    
    if rClay <= obsRobotClayCost:
        dayNeed = max(1, (max(0, clayRobotCost - ore) + rOre - 1) // rOre + 1)
        best = max(best, deepSearch(rOre, rClay + 1, rObs, rGeod,
                                      ore + rOre * dayNeed - clayRobotCost, clay + rClay * dayNeed, obs + rObs * dayNeed, geod + rGeod * dayNeed,
                                      days - dayNeed, rGeod, best))

    if rOre <= max(clayRobotCost, oreRobotCost, obsRobotOreCost, geodeRobotOreCost):
        dayNeed = max(1, (max(0, oreRobotCost - ore) + rOre - 1) // rOre + 1)
        best = max(best, deepSearch(rOre + 1, rClay, rObs, rGeod,
                                      ore + rOre * dayNeed - oreRobotCost, clay + rClay * dayNeed, obs + rObs * dayNeed, geod + rGeod * dayNeed,
                                      days - dayNeed, rGeod, best))

    return best

def calcBest(sourceLines, minutes):
    bests = []
    for line in sourceLines:
        parts = line.split(' ')
        
        global oreRobotCost
        global clayRobotCost
        global obsRobotOreCost
        global obsRobotClayCost
        global geodeRobotOreCost
        global geodeRobotObsCost

        oreRobotCost = int(parts[6])
        clayRobotCost = int(parts[12])
        obsRobotOreCost = int(parts[18])
        obsRobotClayCost = int(parts[21])
        geodeRobotOreCost = int(parts[27])
        geodeRobotObsCost = int(parts[30])

        bests.append(deepSearch(1, 0, 0, 0, 0, 0, 0, 0, minutes, 0, 0))
        
        print('Calculating...')
    return bests

bestsPart1 = calcBest(open('input.txt').read().split('\n'), 24)
bestsPart2 = calcBest(open('input.txt').read().split('\n')[:3], 32)

print('Part 1: {}'.format(sum([(idx + 1) * val for idx, val in enumerate(bestsPart1)])))    # 1177
print('Part 2: {}'.format(reduce(mul, bestsPart2)))                                         # 62744