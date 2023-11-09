def mixing(rounds, decKey):
    input = [int(v) * decKey for v in open('input.txt').read().split('\n')]
    mixed = [v for v in enumerate(input)]
    queue = mixed[:] * rounds
    zeroPair = (input.index(0), 0)

    for v in queue:
        index = mixed.index(v)
        newIndex = (index + mixed[index][1]) % (len(mixed) - 1)

        if newIndex < index:
            mixed = mixed[:newIndex] + [mixed[index]] + mixed[newIndex:index] + mixed[index + 1:]
        elif newIndex > index:
            mixed = mixed[:index] + mixed[index + 1:newIndex + 1] + [mixed[index]] + mixed[newIndex + 1:]

    return sum([mixed[(mixed.index(zeroPair) + index) % len(mixed)][1] for index in [1000, 2000, 3000]])

print('Part 1: {}'.format(mixing(1, 1)))            # 9866
print('Part 2: {}'.format(mixing(10, 811589153)))   # 12374299815791