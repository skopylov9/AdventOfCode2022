import functools

detections = []
for line in open('input.txt').read().split('\n'):
    line = line.replace('x=', '').replace('y=', '')
    line = line.replace('Sensor at ', '').replace(' closest beacon is at ', '')
    sensor, beacon = line.split(':')
    detections.append(([int(coord) for coord in sensor.split(', ')], [int(coord) for coord in beacon.split(', ')]))

detections = sorted(detections, key=lambda detection: detection[0][0])

class Range:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __lt__(self, other):
        if self.l == other.l:
            return self.r < other.r
        return self.l < other.l
    
    def __eq__(self, other):
        return self.l == other.l and self.r == other.r
    
    def intersect(self, other):
        return not (self.l > other.r or self.r < other.l)
    
    def intersected(self, other):
        return Range(min(self.l, other.l), max(self.r, other.r))
    
    def len(self):
        return self.r - self.l

def checkForY(y):
    ranges = []
    for sensor, beacon in detections:
        radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        rangeSize = 2 * (radius - abs(sensor[1] - y)) + 1
        if rangeSize > 0:
            newRange = Range(sensor[0] - rangeSize // 2, sensor[0] + rangeSize // 2 + 1)
            while ranges and newRange.intersect(ranges[-1]):
                newRange = newRange.intersected(ranges.pop(-1))
            ranges.append(newRange)

    return ranges

beaconsInY = set([tuple(beacon) for _, beacon in detections if beacon[1] == 2_000_000])
print('Part 1:', sum([range.len() for range in checkForY(2_000_000)]) - len(beaconsInY))

for y in range(4_000_000):
    if y % 1_00_000 == 0:
        print('Part 2 progress:', y)
    
    ranges = checkForY(y)

    if len(ranges) > 1:
        print('Part 2', ranges[0].r * 4_000_000 + y)
        break