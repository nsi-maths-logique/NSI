class automate_borne:
    def __init__(self, data):
        self.data = data
        self.indice = 0
    def lire(self):
        return self.data[self.indice]
    def ecrire(self, car):
        self.data[self.indice] = car
    def droite(self):
        self.indice += 1
    def gauche(self):
        self.indice -= 1
    def fin(self):
        print(self.data)
        self.indice = 0
    def action(self):
        #etat 1
        while self.lire() != '#':
            self.droite()
        self.droite()
        #etat 2
        while self.lire() != '#':
            self.droite()
        self.gauche()
        #etat 3
        while self.lire() != 0:
            if self.lire() == '#':
                self.droite()
            if self.lire() == 1:
                self.ecrire(0)
                self.gauche()
        self.ecrire(1)
        self.gauche()
        #etat 4
        self.fin()

plus_1 = automate_borne(['#',0,0,0,0,0,0,0,0,'#'])
for i in range(10):
    plus_1.action()
