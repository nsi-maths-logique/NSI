import os
import time

class jeu_de_la_vie:
    '''Classe implantant le jeu de de la vie de Conway'''
    plein = '▮'
    vide = ' '
    def __init__(self, longueur, taille, positif):
        self.longueur = longueur
        self.taille = taille
        self.positif = positif
        self.value = []
        for i in range(longueur):
            if i in positif:
                self.value.append(jeu_de_la_vie.plein)
            else:
                self.value.append(jeu_de_la_vie.vide)
    def n(self, i):
        '''case située au nord'''
        if i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille] == jeu_de_la_vie.plein)
    def s(self, i):
        '''case située au sud'''
        if i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille] == jeu_de_la_vie.plein)
    def o(self, i):
        '''case située à l'ouest'''
        if i % self.taille == 0:
            return 0
        else:
            return int(self.value[i - 1] == jeu_de_la_vie.plein)
    def e(self, i):
        '''case située à l'est'''
        if i % self.taille == self.taille - 1 :
            return 0
        else:
            return int(self.value[i + 1] == jeu_de_la_vie.plein)
    def no(self, i):
        '''case située au nord-ouest'''
        if i % self.taille == 0 or i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille - 1] == jeu_de_la_vie.plein)
    def ne(self, i):
        '''case située au nord-est'''
        if i % self.taille == self.taille - 1 or i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille + 1] == jeu_de_la_vie.plein)
    def so(self, i):
        '''case située au soud-ouest'''
        if i % self.taille == 0 or i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille - 1] == jeu_de_la_vie.plein)
    def se(self, i):
        '''case située au sud-est'''
        if i % self.taille == self.taille - 1 or i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille + 1] == jeu_de_la_vie.plein)
    def somme_voisins(self, i):
        '''
        Algorithme des naissances et des morts
        une cellule morte possédant exactement trois voisines vivantes devient vivante : elle naît ;
        une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.
        '''
        somme = self.e(i) + self.o(i) + self.n(i) + self.s(i) + self.no(i) + self.ne(i)+ self.so(i) + self.se(i)
        if self.value[i] == jeu_de_la_vie.vide and somme == 3:
            return jeu_de_la_vie.plein
        if self.value[i] == jeu_de_la_vie.plein and somme not in [2,3]:
            return jeu_de_la_vie.vide
        return self.value[i]
    def __str__(self):
        out = ''
        for i in range(len(self.value)):
            if i % self.taille == 0:
                out += "\n" + self.value[i]
            else:
                out += self.value[i]
        return out
    def maj(self):
        '''calcul de la nouvelle jeu_de_la_vie'''
        mat = []
        for i in range(len(self.value)):
            mat.append(self.somme_voisins(i))
        out = []
        for i, elem in enumerate(mat):
            if elem == jeu_de_la_vie.plein:
                out.append(i)
        return jeu_de_la_vie(len(mat), self.taille, out)
    def anime(self):
        '''fonction d'animation du jeu de Conway'''
        mem = []
        jeu = self
        while mem != jeu.value:
            os.system('cls')
            mem = jeu.value
            print(jeu)
            time.sleep(.2)
            jeu = jeu.maj()
#developpement
tab_developpement =  [448, 450, 479, 481, 510, 511, 512]
developpement = jeu_de_la_vie(961, 31, tab_developpement)
#oscillateur
tab_oscillateur = [5, 6, 7, 8, 9, 10]
oscillateur = jeu_de_la_vie(16, 4, tab_oscillateur)
#stable
tab_stable = [0, 1, 2, 3, 12, 13, 14, 15]
stable = jeu_de_la_vie(16, 4, tab_stable)
#canon
tab_canon = [54, 55, 93, 132, 146, 163, 172, 185, 186, 202, 203, 212, 228, 229, 253, 268, 269, 270, 277, 294, 295, 308, 309, 316, 317, 345, 346, 386]
canon = jeu_de_la_vie(800, 40, tab_canon)

jeux = [developpement, oscillateur, stable, canon]
jeu = jeux[3]
jeu.anime()


