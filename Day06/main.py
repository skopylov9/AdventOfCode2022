signal = open("input.txt").read()

for i in range(len(signal)):
    if len(set(signal[i : i + 14])) == 14:
        print(i + 14)
        break