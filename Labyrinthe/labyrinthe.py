import random

class labyrinthe():
    def __init__(self, *value):
        self.nb_lignes = 10
        self.nb_colonnes = 10
        self.taille = self.nb_lignes * self.nb_colonnes
        self.arrivee = self.taille - 1
        self.labyrinthe = []
        if len(value) > 0:
            self.labyrinthe = 'oxxxxxxxxxooooooooxxxxxxxxxoxxxxooooxoxxxxoxxoxoxxooooooxoxxoxoxxxxoxxoxooooooxxoxxxxxxxxxoooooooooo'
        else:
            for i in range(0, self.taille):
                self.labyrinthe.append(__class__.hasard())
            self.labyrinthe[0] = 'o'
            self.labyrinthe[self.arrivee] = 'o'
    def hasard():
        result = random.random()
        if result <= 0.3:
            return 'x'
        return 'o'
    def above(self, index):
        if index < self.nb_colonnes:
            return set()
        if set(self.labyrinthe[index - self.nb_colonnes]) == 'x':
            return set()
        return {index - self.nb_colonnes}
    def right(self, index):
        if index % self.nb_colonnes == self.nb_colonnes - 1:
            return set()
        if self.labyrinthe[index + 1] == 'x':
            return set()
        return {index + 1}
    def below(self, index):
        if index >= self.taille - self.nb_colonnes:
            return set()
        if self.labyrinthe[index + self.nb_colonnes] == 'x':
            return set()
        return {index + self.nb_colonnes}
    def left(self, index):
        if index % self.nb_colonnes == 0:
            return set()
        if self.labyrinthe[index - 1] == 'x':
            return set()
        return {index - 1}
    def succ(self, index):
        return self.above(index) | self.right(index) | self.below(index) | self.left(index)
    def ens_succ(self, ens):
        out = set()
        for elem in ens:
            out = out | self.succ(elem)
        return out
    def parcours(self):
        i = 0
        stack = []
        stack.append({0})
        if self.ens_succ(stack[i]) == set():
            return stack
        while stack[i] != self.ens_succ(stack[i]):
            stack.append(stack[i] | self.ens_succ(stack[i]))
            i = i + 1
        return stack
    def show(self):
        out = 'Labyrinthe :'
        for i in range(0, self.taille):
            if i % self.nb_colonnes == 0:
                out += '\n'
            out += self.labyrinthe[i]
        return out
    def resoudre(self):
        print(self.show())
        chemin_existe = self.arrivee in self.parcours()[-1]
        print("Il y a au moins %d parcours qui mene a l'arrivee" %chemin_existe)
        
mylab = labyrinthe()
mylab.resoudre()