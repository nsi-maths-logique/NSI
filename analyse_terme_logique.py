import regex

#def langage
#variables : x1,x2,...
var = 'x\d*'
#on considere que les constantes sont des fonctions d'arite 0
#l'arite des fonctions est definie par leur position dans le tableau fonctions
fonctions = ['c\d*','f\d*','g\d*','h\d*','i\d*','j\d*','k\d*']

def suite(tab):
    '''
    determine les positions des caracteristiques de chaque fonction dans le tableau retourne par findall
    calcul de la suite u0 = 2 et un+1 = un + n + 1 
    '''
    borne = len(tab) - 1
    out = [2]
    for i in range(1, borne):
        out.append(out[i-1] + i + 1)
    return out

def bien_forme(terme):
    reg = f"{var}|{fonctions[0]}"
    i = 1
    while i < len(fonctions):
        arite = ',(?R)'*(i-1)
        fonction_i_aire = f"|{fonctions[i]}\((?R){arite}\)"
        reg += fonction_i_aire
        i += 1
    return terme == regex.search(reg, terme)[0]


def analyse(terme):
    terme = terme.replace(' ','')
    assert bien_forme(terme), "L'expression n'est pas bien formee"
    reg = f"({var})|({fonctions[0]})"
    i = 1
    while i < len(fonctions):
        arite = ',((?R))'*(i-1)
        fonction_i_aire = f"|({fonctions[i]})\(((?R)){arite}\)"
        reg += fonction_i_aire
        i += 1
    matches = regex.findall(reg, terme)[0]
    if matches[0] != '':
        type = 'variable'
        name = matches[0]
        resultat = []
        return (type, name, resultat)
    if matches[1] != '':
        type = 'constante'
        name = matches[1]
        resultat = []
        return (type, name, resultat)
    for i, value in enumerate(suite(fonctions)):
        if matches[value] != '':
            resultat = f'[matches[{value+1}]'
            type = 'fonction'
            name = matches[value]
            j = i
            k = value + 1
            while j > 0:
                k += 1
                resultat += f',matches[{k}]'
                j -= 1
            resultat += ']'
            resultat = eval(resultat)
            return (type, name, resultat)

class terme:
    def __init__(self, data):
        resultat = analyse(data)
        self.texte = data.replace(' ', '')
        self.type = resultat[0]
        self.name = resultat[1]
        self.args = resultat[2]
    def __eq__(self, other):
        return self.texte == other.texte
    def __len__(self):
        if self.type == 'constante' or self.type == 'variable':
            return 0
        else:
            return len(self.args)
    def __str__(self, tab = ''):
        out = f'- <{self.type}>({len(self)}) : {self.name}\n'
        tab += '\t'
        for elem in self.args:
            t_elem = terme(elem)
            out += tab + t_elem.__str__(tab)
        return out
    def sous_termes(self):
        if self.type == 'constante' or self.type == 'variable':
            return {self.texte}
        else:
            out = {self.texte}
            for elem in self.args:
                t_elem = terme(elem)
                out = out | t_elem.sous_termes()
            return out
    def sous_termes_propres(self):
        return self.sous_termes() - {self.texte}

t1 = terme("h(x,f(c),c1)")
t2 = terme("h(f(x1),x1,c1)")
print(t1.unifie(t2).texte)
