class Calcu:
    def suma(self, a, b):
        print (a + b)

    def resta(self, a, b):
        print(a - b)

    def multiplicacion(self, a, b):
        print(a * b)

    def division(self, a, b):
        print(a / b)

    def primo(self, n):
        prime = True
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    prime = False
        print(f'{n} es numero primo ? {prime}')

    def fibb(self, n):
        a = 0
        b = 1
        print(a), print(b)
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(c)

    def par_non(self, n):
        if n % 2 == 0:
            print(f'{n} es par')
        else:
            print(f'{n} es non')


Diego = Calcu()
Diego.primo(9)