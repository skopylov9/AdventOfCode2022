commands = open("input.txt").read().split('\n')

def parseCommands(commands):
    dirTree = []
    deep = 0
    for i in range(len(commands)):
        command = commands[i]
        if command.startswith('dir') or command.startswith('$ ls'):
            continue
        if command.startswith('$ cd /'):
            continue
        if command.startswith('$ cd ..'):
            if deep == 0:
                break
            deep -= 1
        elif command.startswith('$ cd '):
            if deep == 0:
                dirTree.append(parseCommands(commands[i + 1 :]))
            deep += 1
        if deep == 0 and not command.startswith('$'):
            dirTree.append(int(command.split(' ')[0]))
    return dirTree

root = parseCommands(commands)

dirSizes = []
def calcDirSizes(root):
    innerDirsSize = sum([calcDirSizes(element) for element in root if isinstance(element, list)])
    innerFilesSize = sum([element for element in root if not isinstance(element, list)])
    dirSizes.append(innerDirsSize + innerFilesSize)
    return dirSizes[-1]
calcDirSizes(root)

print(sum([size for size in dirSizes if size < 100_000]))
print(min([size for size in dirSizes if size > (dirSizes[-1] - 40_000_000)]))
