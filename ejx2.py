def palindromo(x):
    pal = False
    va = x.replace(' ', '')
    viene = va[::-1]
    if va == viene:
        pal = True
    print(pal)


palindromo('anita lava la tina')


def arreglo(z):
    entrada = z
    resultado = ' '.join(sorted(entrada.split(), key = str.casefold))
    print(resultado)

arreglo('el perro baila kumbia los martes')

def lista_elementos(busqueda, item):
    indice = list()
    for i in range(len(busqueda)):
        if busqueda[i] == item:
            indice.append([i])
        elif isinstance(busqueda[i], list):
            for index in lista_elementos((busqueda[i], item)):
                indice.append([i] + index)
    print(indice)

lista_elementos([1, 2, 3], 1)
