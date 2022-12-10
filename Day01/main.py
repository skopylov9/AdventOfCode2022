fileData = open("input.txt").read()

byElfsCalories = [sum([int(calories) for calories in list.split('\n')]) for list in fileData.split('\n\n')]

print(max(byElfsCalories), sum(sorted(byElfsCalories)[-3:]))
