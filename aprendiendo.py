from random import randint
from collections import Counter

def tiro_de_dado(*dado, intentos=1_000_000):
    contador = Counter()
    for tiro in range(intentos):
        contador[sum((randint(1,sides) for sides in dado))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dado),sum(dado)+1):
        print('{}\t{:0.2f}%'.format(outcome, contador[outcome]*100/intentos))


def dice_roll():
    print(randint(1,6))

tiro_de_dado(2)