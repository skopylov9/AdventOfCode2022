def decimalToSnafu(decimal):
    value = ''
    while decimal:
        value += str(decimal % 5)
        decimal = (decimal // 5) + (1 if decimal % 5 > 2 else 0)
    return value.replace('3', '=').replace('4', '-')[::-1]

def snafuToDecimal(snafuStr):
    value = 0
    for idx, ch in enumerate(snafuStr[::-1]):
        value += pow(5, idx) * int(ch.replace('-', '-1').replace('=', '-2'))
    return value

print('Part 1: {}'.format(decimalToSnafu(sum([snafuToDecimal(snafuNumber) for snafuNumber in open('input.txt').read().split('\n')]))))  # 122-12==0-01=00-0=02
