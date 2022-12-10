commands = open("input.txt").read().split('\n')

class CRT:
    X = 1
    cycle = 0
    matrix = []
    signalStrenghts = 0

    def addx(self, value):
        self.X += value
    
    def nextCycle(self):
        self.cycle += 1
        if self.cycle in range(20, 221, 40):
            self.signalStrenghts += self.cycle * self.X
        
        if (self.cycle - 1) % 40 == 0:
            self.matrix.append([])
        
        self.matrix[-1].append("#" if self.cycle % 40 in range(self.X, self.X + 3) else ".")

crt = CRT()
for command in commands:
    if command.startswith("noop"):
        crt.nextCycle()
    if command.startswith("addx"):
        crt.nextCycle()
        crt.nextCycle()
        crt.addx(int(command.split(' ')[1]))

print(crt.signalStrenghts)
for line in crt.matrix:
    print("".join(line))  
