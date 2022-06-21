def factores_primos(n):
    primo = True
    cont = 0
    a = 0
    prime_list = []
    resultado = list()
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                cont = i
                cont = max(i, cont)




    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime_list.append(i)

    for i in prime_list:
        for e in range(2, i):
            if i % e == 0:
                try:
                    prime_list.remove(i)
                except:
                    pass


    for i in prime_list:
        while n % i == 0:
            n = n / i
            resultado.append(i)





    print(resultado)

factores_primos(120)
