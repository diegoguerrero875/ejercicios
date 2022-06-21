class carro:
    motor = False
    llantas = False
    frenoDeMano = True

    def checkLlanta(self):
        self.llantas = True

    def prenderCarro(self):
        self.motor = True

    def quitarFreno(self):
        self.frenoDeMano = False

    def acelerar(self):
        return(f'{"el motor esta prendido" if self.motor else "el motor esta apagado"}')
        #if self.motor == False:
         #   print('el motor no esta prendido')
        #elif self.frenoDeMano == True:
         #   print('el freno de mano esta puesto, quitalo')
        #else:
         #   print('el carro comienza a acelerar')

    def __repr__(self):
        return (f'{"prendido" if self.motor else "apagado"} ')

    def __init__(self, marca):
        self.marca = marca


mamalona = carro('Toyota')
mamalona.prenderCarro()
print(mamalona.acelerar())


