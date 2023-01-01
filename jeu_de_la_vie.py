from random import choices
import os
import time

class matrice:
    plein = '▮'
    vide = ' '
    def __init__(self, longueur, taille, positif):
        self.longueur = longueur
        self.taille = taille
        self.positif = positif
        self.value = []
        for i in range(longueur):
            if i in positif:
                self.value.append(matrice.plein)
            else:
                self.value.append(matrice.vide)
    def n(self, i):
        if i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille] == matrice.plein)
    def s(self, i):
        if i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille] == matrice.plein)
    def o(self, i):
        if i % self.taille == 0:
            return 0
        else:
            return int(self.value[i - 1] == matrice.plein)
    def e(self, i):
        if i % self.taille == self.taille - 1 :
            return 0
        else:
            return int(self.value[i + 1] == matrice.plein)
    def no(self, i):
        if i % self.taille == 0 or i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille - 1] == matrice.plein)
    def ne(self, i):
        if i % self.taille == self.taille - 1 or i < self.taille:
            return 0
        else:
            return int(self.value[i - self.taille + 1] == matrice.plein)
    def so(self, i):
        if i % self.taille == 0 or i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille - 1] == matrice.plein)
    def se(self, i):
        if i % self.taille == self.taille - 1 or i >= self.longueur - self.taille:
            return 0
        else:
            return int(self.value[i + self.taille + 1] == matrice.plein)
    def somme_voisins(self, i):
        '''
        Algorithme des naissances et des morts
        une cellule morte possédant exactement trois voisines vivantes devient vivante : elle naît ;
        une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt.
        '''
        somme = self.e(i) + self.o(i) + self.n(i) + self.s(i) + self.no(i) + self.ne(i)+ self.so(i) + self.se(i)
        if self.value[i] == matrice.vide and somme == 3:
            return matrice.plein
        if self.value[i] == matrice.plein and somme not in [2,3]:
            return matrice.vide
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
        mat = []
        for i in range(len(self.value)):
            mat.append(self.somme_voisins(i))
        out = []
        for i, elem in enumerate(mat):
            if elem == matrice.plein:
                out.append(i)
        return matrice(len(mat), self.taille, out)
    def anime(self):
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
developpement = matrice(961, 31, tab_developpement)
#oscillateur
tab_oscillateur = [5, 6, 7, 8, 9, 10]
oscillateur = matrice(16, 4, tab_oscillateur)
#stable
tab_stable = [0, 1, 2, 3, 12, 13, 14, 15]
stable = matrice(16, 4, tab_stable)
#canon
tab_canon = [54, 55, 93, 132, 146, 163, 172, 185, 186, 202, 203, 212, 228, 229, 253, 268, 269, 270, 277, 294, 295, 308, 309, 316, 317, 345, 346, 386]
canon = matrice(800, 40, tab_canon)

jeux = [developpement, oscillateur, stable, canon]
jeu = jeux[3]
jeu.anime()
