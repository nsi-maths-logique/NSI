class application:
    def __init__(self, nom, definition, domaine, image):
        self.nom = nom
        self.definition = definition
        self.domaine = domaine
        self.image = image
        self.arite = len(max(definition)) - 1
    def __call__(self, *arg):
        for tuple in self.definition:
            if tuple[:len(tuple)-1] == arg:
                return tuple[-1]
        return None
    def est_injective(self):
        count = {}
        for elem in self.image:
            count[elem] = 0
        for tuple in self.definition:
            count[tuple[-1]] += 1
            if count[tuple[-1]] > 1:
                return False
        return True
    def est_surjective(self):
        count = {}
        for elem in self.image:
            count[elem] = 0
        for tuple in self.definition:
            count[tuple[-1]] += 1
        for clef, valeur in count.items():
            if valeur == 0:
                return False
        return True
    def est_bijective(self):
        return self.est_injective() & self.est_surjective()
    def est_une_restriction(self, other):
       return self.domaine.issubset(other.domaine) & self.definition.issubset(other.definition)
    def est_une_extension(self, other):
        return other.est_une_restriction(self)

Domaine_F = {1,2,3,4}
Image_F = {2,4,6,8}
Def_F = {(1,2),(2,4),(3,6),(4,8)}
F = application('F', Def_F, Domaine_F, Image_F)

Domaine_G = {1,2,3,4}
Image_G = {2,4,6,8}
Def_G = {(1,2),(2,4),(3,6)}
G = application('G', Def_G, Domaine_G, Image_G)

Domaine_H = {1,2,3,4}
Image_H = {2,4,6,8}
Def_H = {(1,2),(2,4),(3,4)}
H = application('H', Def_H, Domaine_H, Image_H)

Domaine_I = {(x, y) for x in Domaine_F for y in Domaine_F}
Image_I = {2,4,6,8}
Def_I = {(x, y, z) for x in Domaine_F for y in Domaine_F for z in Image_F if z == x + y}
I = application('I', Def_I, Domaine_I, Image_I)

Domaine_J = Domaine_F
Image_J = Image_F
Def_J = {x for x in Def_F if x != (4,8)}
J = application('J', Def_J, Domaine_J, Image_J)

Ens_application = {F, G, H, I, J}

for app in Ens_application:
    print('\nFonction %s :'%app.nom)
    print('--------------')
    print('Domaine : ', app.domaine)
    print('Image : ', app.image)
    print('Definition : ', app.definition)
    print('Arite : ', app.arite)
    if app.arite > 1:
        out = list(map(lambda x: app.nom + '(' + str(x) + ')=' + str(app(*(x))), app.domaine))
    else:
        out = list(map(lambda x: app.nom + '(' + str(x) + ')=' + str(app(x)), app.domaine))
    print("Exemples d'appels : %s"%('\t').join(out[1:5]))
    print('Injective : ', app.est_injective())
    print('Surjective : ', app.est_surjective())
    print('Bijective : ', app.est_bijective())

print('\nRestriction :')
print('--------------')
for couple in {(x,y) for x in Ens_application for y in Ens_application}:
    print('%s est une restriction de %s : '%(couple[0].nom, couple[1].nom), couple[0].est_une_restriction(couple[1]))
    print('%s est une restriction de %s : '%(couple[1].nom, couple[0].nom), couple[1].est_une_restriction(couple[0]))

