input = [line.replace(':', '').split(' ') for line in open('input.txt').read().split('\n')]

operationMap = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a / b,
    }

backOperationMapL = {
    '+' : lambda a, b: a - b,
    '-' : lambda a, b: a + b,
    '*' : lambda a, b: a / b,
    '/' : lambda a, b: a * b,
    }

backOperationMapR = {
    '+' : lambda a, b: a - b,
    '-' : lambda a, b: b - a,
    '*' : lambda a, b: a / b,
    '/' : lambda a, b: b / a,
    }

equationDependency = dict()
rootEquation = dict()
for line in input:
    if len(line) > 2:
        equationDependency[line[1]] = line[0]
        equationDependency[line[3]] = line[0]
        rootEquation[line[0]] = (line[1], line[3], operationMap[line[2]])
    else:
        rootEquation[line[0]] = tuple([line[1]])

humnEquation = rootEquation.copy()

remNodeKey = 'humn'
while remNodeKey != 'root':
    humnEquation.pop(remNodeKey)
    remNodeKey = equationDependency[remNodeKey]

for line in input:
    if len(line) <= 2:
        continue
    operation = line[2]
    if line[0] == 'root':
        operation = '-'
    if line[1] not in humnEquation:
        humnEquation[line[1]] = (line[0], line[3], backOperationMapL[operation])
    if line[3] not in humnEquation:
        humnEquation[line[3]] = (line[0], line[1], backOperationMapR[operation])

humnEquation['root'] = tuple(['0'])

def solve(node, equation):
    if len(equation[node]) == 1:
        return float(equation[node][0])
    return equation[node][2](solve(equation[node][0], equation), solve(equation[node][1], equation))

print('Part 1: {}'.format(solve('root', rootEquation)))  # 81075092088442
print('Part 2: {}'.format(solve('humn', humnEquation)))  # 3349136384441
