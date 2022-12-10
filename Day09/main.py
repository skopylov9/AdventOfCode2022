def fixTailPosition(head, tail):
    normolize = lambda value: 0 if not value else 1 if value > 0 else -1
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return (tail[0] + normolize(head[0] - tail[0]), tail[1] + normolize(head[1] - tail[1]))
    return tail

def makeMove(head, move):
    transformer = {
        'R':lambda pos: (pos[0], pos[1] + 1),
        'L':lambda pos: (pos[0], pos[1] - 1),
        'U':lambda pos: (pos[0] - 1, pos[1]),
        'D':lambda pos: (pos[0] + 1, pos[1]),
    }
    return transformer[move](head)

def goThroughMoves(knots, moves):
    visited = set()
    for move in moves:
        for j in range(int(move[1])):
            knots[0] = makeMove(knots[0], move[0])
            for i in range(1, len(knots)):
                knots[i] = fixTailPosition(knots[i - 1], knots[i])
            visited.add(knots[-1])
    return visited

moves = [move.split(' ') for move in open("input.txt").read().split('\n')]
print("Part 1: ", len(goThroughMoves([(0, 0) for i in range(2)], moves)))
print("Part 2: ", len(goThroughMoves([(0, 0) for i in range(10)], moves)))
