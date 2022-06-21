class Ninja:
    def __init__(self, HP, ATK, DEF):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

    ataqueEntrante = 0
    ataqueSalida = 0

    def __repr__(self):
        return (f'eres un ninja con {self.HP} de vida'
                f', {self.ATK} de Ataque '
                f'y {self.DEF} de Defensa')

    def dmg(self, x):
        self.ataqueEntrante = x
        self.HP = self.HP - (self.ataqueEntrante - self.DEF)


#tortuga = Ninja (100, 5, 5)
#print(tortuga)
#tortuga.dmg(20)
#print(tortuga)
#tortuga.dmg(20)
#print(tortuga)


