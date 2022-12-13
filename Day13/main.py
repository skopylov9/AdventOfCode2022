class Item:
    def __init__(self, value):
        self.value = value
    
    def transform(self, other):
        if isinstance(self.value, int) and isinstance(other.value, int):
            return self.value
        return [Item(v) for v in self.value] if isinstance(self.value, list) else [Item(self.value)]
    
    def __lt__(self, other):
        return self.transform(other) < other.transform(self)
    
    def __gt__(self, other):
        return self.transform(other) > other.transform(self)
    
    def __eq__(self, other):
        return self.transform(other) == other.transform(self)

pairs = [pair.split('\n') for pair in open('input.txt').read().split('\n\n')]
pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]
print("Part 1:", sum([i + 1 for i in range(len(pairs)) if Item(pairs[i][0]) < Item(pairs[i][1])]))

packets = sorted([Item(packet) for pair in pairs for packet in pair] + [Item([[2]]), Item([[6]])])
print("Part 2:", (packets.index(Item([[2]])) + 1) * (packets.index(Item([[6]])) + 1))
    