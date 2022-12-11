import copy
from functools import reduce

class Monkey:
    def __init__(self, description) -> None:
        id, items, operation, test, ifTrue, ifFalse = description.split('\n')
        self.id = int(id[7:8])
        self.items = [int(item) for item in items[18:].split(', ')]
        self.test = int(test[21:])
        self.ifTrue = int(ifTrue[29:])
        self.ifFalse = int(ifFalse[30:])
        self.activity = 0

        operation = operation[19:]
        if operation == 'old * old': self.operation = lambda value: value * value
        elif operation[4] == '*': self.operation = lambda value: value * int(operation[6:])
        elif operation[4] == '+': self.operation = lambda value: value + int(operation[6:])

def goThroughRounds(monkeys, rounds, devider):
    for i in range(rounds):
        for monkey in monkeys:
            monkey.activity += len(monkey.items)
            for item in [devider(monkey.operation(item)) for item in monkey.items]:
                monkeys[monkey.ifFalse if item % monkey.test else monkey.ifTrue].items.append(item)
            monkey.items.clear()
    activities = sorted([monkey.activity for monkey in monkeys])
    print(activities[-1] * activities[-2])

monkeys = [Monkey(description) for description in open("input.txt").read().split('\n\n')]
dev = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys])

# Part 1
goThroughRounds(
    copy.deepcopy(monkeys),
    20,
    lambda value: value // 3)

# Part 2
goThroughRounds(
    copy.deepcopy(monkeys),
    10000,
    lambda value: value % dev if value // dev else value)
