import time
import random

def juego_tiempo():
    target = random.randint(2, 4) #segundos a esperar
    print('\n Tu tiempo es {} segundos'.format(target))

    input(' ---Presiona ENTER para comenzar--- ')
    start = time.perf_counter()

    input('\nPresiona ENTER de nuevo en {} segundos...'.format(target))
    enlazado = time.perf_counter() - start

    print('\nTiempo enlazado: {0:.3f} segundos'.format(enlazado))
    if enlazado == target:
        print('Felicidades timing perfecto !')
    elif enlazado < target:
        print('({0:.3f} segundos mas rapido de lo esperado)'.format(target - enlazado))
    else:
        print('({0:.3f} segundos mas lento de lo esperado)'.format(enlazado - target))

juego_tiempo()