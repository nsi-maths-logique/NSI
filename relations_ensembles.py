import regex
from regex import *

class relation:
    '''Implantation des relations a la facon ensembliste'''
    def __init__(self, nom, domaine, image, definition, variables):
        self._nom = nom
        self._domaine = domaine
        self._image = image
        self._definition = definition
        if not self._est_vide():
            self._arite = len(max(definition))
        else:
            self._arite = 0
        self._variables = variables
    def __call__(self, *arg):
        nb_var = 0
        motif_resultat = '('
        motif_tuple = '('
        motif_domaine = ''
        for index, elem in enumerate(arg):
            if elem not in self._domaine:
                motif_tuple += elem + ','
                motif_resultat += elem + ','
                motif_domaine += 'for %s in %s '%(elem, self._domaine)
                nb_var += 1
            else:
                motif_tuple += str(elem) + ','
        motif_tuple = motif_tuple[0:-1] + ')'
        motif_resultat = motif_resultat[0:-1] + ')'
        if nb_var == 0:
            return arg in self._definition
        else:
            return eval('{%s %s if %s in %s}'%(motif_resultat, motif_domaine, motif_tuple, self._definition))
    def _projection(self, i):
        motif = '('
        for index in range(self._arite):
            motif += 'x' + str(index) + ','
        motif = motif[0:-1] + ')'
        return eval('{%s for %s in %s}'%('x' + str(i), motif, self._definition))
    def _est_vide(self):
        return self._definition == set()
    def _est_pleine(self):
        Domaine = self._domaine
        Image = self._image
        motif_tuple = '('
        motif_domaine = ''
        for i in range(self._arite-1):
            motif_tuple += 'x' + str(i) + ','
            motif_domaine += 'for x' + str(i)  + ' in %s '%(self._domaine)
        motif_tuple +=  'y)'
        Definition = eval('{%s %s for y in %s}'%(motif_tuple, motif_domaine, self._image))
        return self._definition == Definition
    def __EQ__(self, other):
        return self._definition == other._definition
    def __NE__(self, other):
        return not self == other
    def __lt__(self, other):
        return self._definition.issubset(other._definition) and self._definition != other._definition
    def __le__(self, other):
        return self._definition.issubset(other._definition)
    def __gt__(self, other):
        return other < self
    def __ge__(self, other):
        return not self < other
    def __or__(self, other):
        Domaine = self._domaine | other._domaine
        Image = self._image | other._image
        Definition = self._definition | other._definition
        return relation("%s|%s"%(self._nom, other._nom), Domaine, Image, Definition, self._variables)
    def __and__(self, other):
        Domaine = self._domaine | other._domaine
        Image = self._image | other._image
        Definition = self._definition & other._definition
        return relation("%s&%s"%(self._nom, other._nom), Domaine, Image, Definition, self._variables)
    def __sub__(self, other):
        Domaine = self._domaine | other._domaine
        Image = self._image | other._image
        Definition = self._definition - other._definition
        return relation("%s-%s"%(self._nom, other._nom), Domaine, Image, Definition, self._variables)
    def __neg__(self):
        Domaine = self._domaine
        Image = self._image
        motif_tuple = '('
        motif_domaine = ''
        for i in range(self._arite-1):
            motif_tuple += 'x' + str(i) + ','
            motif_domaine += 'for x' + str(i)  + ' in %s '%(self._domaine)
        motif_tuple +=  'y)'
        Definition = eval('{%s %s for y in %s if %s not in %s}'%(motif_tuple, motif_domaine, self._image, motif_tuple, self._definition))
        return relation("-%s"%(self._nom), Domaine, Image, Definition, self._variables)
    def show(self):
        print('Relation : ', self._nom)
        print('Domaine : ', self._domaine)
        print('Image : ', self._image)
        print('Definition : ', self._definition)
        print('Arite : ', self._arite)

X = 'x0'
Y = 'x1'
Z = 'x2'
Variables = {X, Y, Z}
Domaine_R = {1,2,3,4,6}
Image_R = {2,3,4,6,8}
Def_R = {(1,1,2),(1,2,2),(2,2,4)}
R = relation('R', Domaine_R, Image_R, Def_R, Variables)

Domaine_S = {1,2}
Image_S = {2}
Def_S = {(1,1,2),(1,2,2)}
S = relation('S', Domaine_S, Image_S, Def_S, Variables)

R.show()
print('R(X,X,2) : ', R(X,X,2))
print('R(X,1,2) : ', R(X,1,2))
print('R(1,1,2) : ', R(1,1,2))
print('R(2,1,2) : ', R(2,1,2))
print('S < R : ', S < R)
print('(R&S) < R : ', (R&S) < R)
print('R <= (R|S) : ', R <= (R|S))
print('(-R|R)._est_pleine() : ', (-R|R)._est_pleine())
print('(-R&R)._est_pleine() : ', (-R&R)._est_vide())
print('R._projection(0) : ', R._projection(0))
