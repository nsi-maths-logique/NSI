class fonction:
    '''Implantation des fonctions a la facon de la theorie des ensembles, c'est-dire par leur graphe'''
    def __init__(self, nom, definition, domaine, image):
        self.nom = nom
        self.definition = definition
        self.domaine = domaine
        self.image = image
        self.arite = len(max(definition)) - 1
        if self.est_une_fonction():
            raise Exception("Oooops, l'objet defini n'est pas une fonction") 
    def __call__(self, *arg):
        for tuple in self.definition:
            if tuple[:len(tuple)-1] == arg:
                return tuple[-1]
        return None
    def est_injective(self):
        '''verifie que chaque element de l'image a au plus un antecedent'''
        count = {}
        for elem in self.image:
            count[elem] = 0
        for tuple in self.definition:
            count[tuple[-1]] += 1
            if count[tuple[-1]] > 1:
                return False
        return True
    def est_surjective(self):
        '''verifie que chaque element de l'image a au moins un antecedent'''
        count = {}
        for elem in self.image:
            count[elem] = 0
        for _tuple in self.definition:
            count[_tuple[-1]] += 1
        for clef, valeur in count.items():
            if valeur == 0:
                return False
        return True
    def est_bijective(self):
        '''verifie que chaque element de l'image a exactement un antecedent'''
        return self.est_injective() & self.est_surjective()
    def est_une_restriction(self, other):
       return self.domaine.issubset(other.domaine) & self.definition.issubset(other.definition)
    def est_une_extension(self, other):
        return other.est_une_restriction(self)
    def est_une_application(self):
        '''verifie si la fonction est definie sur l'ensemble du domaine'''
        motif = '('
        for i in range(self.arite):
            motif += 'x' + str(i) + ','
        motif_args = motif[0:-1] + ')'
        motif_def = motif + 'y)'
        dom_def = eval('{%s for %s in %s for y in %s}'%(motif_args, motif_def, self.definition, self.image))
        return dom_def == self.domaine
    def est_une_fonction(self):
        '''verifie si un element du domaine a plusieurs images. Dans ce cas, il s'agit d'une relation qui n'est pas une fonction'''
        count = {}
        for elem in self.domaine:
            if self.arite == 1:
                count[elem] = 0
            else:
                count[str(elem)] = 0
        for _tuple in self.definition:
            if self.arite == 1:
                count[_tuple[0]] += 1
            else:
                count[str(_tuple[0:-1])] += 1
        for clef, valeur in count.items():
            if valeur > 1:
                return True
        return False
    def show(self):
        print('\nFonction %s :'%self.nom)
        print('--------------')
        print('Domaine : ', self.domaine)
        print('Image : ', self.image)
        print('Definition : ', self.definition)
        print('Arite : ', self.arite)
        if self.arite > 1:
            out = list(map(lambda x: self.nom + '(' + str(x) + ')=' + str(self(*(x))), self.domaine))
        else:
            out = list(map(lambda x: self.nom + '(' + str(x) + ')=' + str(self(x)), self.domaine))
        print("Exemples d'appels : %s"%('\t').join(out[1:5]))
        print('Injective : ', self.est_injective())
        print('Surjective : ', self.est_surjective())
        print('Bijective : ', self.est_bijective())
        print('Est une application : ', self.est_une_application())

Domaine = {1,2,3,4}
Image = {2,4,6,8}
Def_F = {(1,2),(2,4),(3,6),(4,8)}
F = fonction('F', Def_F, Domaine, Image)


Def_G = {(1,2),(2,4),(3,6)}
G = fonction('G', Def_G, Domaine, Image)

Def_H = {(1,2),(2,4),(3,4)}
H = fonction('H', Def_H, Domaine, Image)

Domaine_I = {(x, y) for x in Domaine for y in Domaine}
Image_I = {2,4,6,8}
Def_I = {(x, y, z) for x in Domaine for y in Domaine for z in Image if z == x + y}
I = fonction('I', Def_I, Domaine_I, Image_I)

Ens_fonctions = {F, G, H, I}
for fonc in Ens_fonctions:
    fonc.show()
print('\nRestriction :')
print('--------------')
for couple in {(x,y) for x in Ens_fonctions for y in Ens_fonctions if x != y}:
    print('%s est une restriction de %s : '%(couple[0].nom, couple[1].nom), couple[0].est_une_restriction(couple[1]))
