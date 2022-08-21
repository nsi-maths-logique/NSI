class Pile():
    class _Noeud:
        def __init__(self, element, suivant):
            self._element = element
            self._suivant = suivant
    def __init__(self):
        self._premier = None
        self._longueur = 0
    def __len__(self):
        return self._longueur
    def est_vide(self):
        return self._longueur == 0
    def tete(self):
        if self.est_vide():
            raise Empty('La pile est vide')
        return self._premier._element
    def empile(self, e):
        #on profite de la strategie de passage par valeur
        self._premier = self._Noeud(e, self._premier)
        self._longueur += 1
    def depile(self):
        if self.est_vide():
            raise Empty('La pile est vide')
        sortie = self._premier._element
        self._premier = self._premier._suivant
        self._longueur -= 1
        return sortie
    def show(self):
        out = ''
        noeud_courant = self._premier
        while noeud_courant != None:
            out += str(noeud_courant._element) + ' -> '
            noeud_courant = noeud_courant._suivant
        out += 'None'
        print(out)

p = Pile()
p.empile(1)
p.empile(2)
p.empile(3)
p.depile()
p.show()

class File():
    class _Noeud:
        def __init__(self, element, suivant):
            self._element = element
            self._suivant = suivant
    def __init__(self):
        self._premier = None
        self._dernier = None
        self._longueur = 0
    def __len__(self):
        return self._longueur
    def est_vide(self):
        return self._longueur == 0
    def premier(self):
        if self.est_vide():
            raise Empty('La file est vide')
        return self._premier._element
    def enfile(self, e):
        nouveau = self._Noeud(e, None)
        if self.est_vide():
            self._premier = nouveau
        else:
            self._dernier._suivant = nouveau
        self._dernier = nouveau
        self._longueur += 1
    def defile(self):
        if self.est_vide():
            raise Empty('La file est vide')
        sortie = self._premier._element
        self._premier = self._premier._suivant
        self._longueur -= 1
        return sortie
    def show(self):
        out = ''
        noeud_courant = self._premier
        while noeud_courant != None:
            out += str(noeud_courant._element) + ' -> '
            noeud_courant = noeud_courant._suivant
        out += 'None'
        print(out)
f = File()
f.enfile(1)
f.enfile(2)
f.enfile(3)
f.defile()
f.show()

