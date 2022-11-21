from algebre_relationnelle import *

def affiche(relations):
    '''
    fonction pour l'affichage et de formatage des relations
    '''
    for i, elem in enumerate(relations):
        formule = elem.traduction()
        x = '\nRelation P%d(%s) ≡ '%(i,','.join(list(map(lambda x: x.name, elem.attributs)))) + elem.name + " :"
        print(x)
        print('-' * (len(x)-1))
        print('P%d = '%i + str(elem))
        print("F(P%d)[%s]"%(i,elem.arguments), '≡', formule)

#Definitions des attributs
A = attribut('A', {'a1','a2','a3','a4'})
B = attribut('B', {'b1','b2','b3','b4'})
C = attribut('C', {'c1','c2','c3','c4'})
D = attribut('D', {'d1','d2','d3'})
E = attribut('E', {'e1','e2','e3'})
a1 = attribut('a1', {'a1'}, True)
xmin, xmax = 0, 10
domaine = range(xmin,xmax)
ext = range(xmin+1,xmax-1)
F = attribut('F', {x for x in domaine})
PAIR = attribut('PAIR', {x for x in domaine if x%2 == 0}, True)
G = attribut('G', {x for x in domaine})
H = attribut('H', {x for x in domaine})

#Definitions des relations
R = relation('R', 'R', 
             {('a1','b1','c1','d1','e1'),
              ('a1','b1','c1','d2','e2'),
              ('a2','b2','c2','d1','e1'),
              ('a3','b3','c3','d2','e2'),
              ('a4','b4','c4','d1','e1'),
              ('a4','b4','c4','d2','e2'),
              ('a4','b4','c4','d3','e3')},
              (A,B,C,D,E))
S = relation('S', 'S', 
             {('a1','b1','c1','d1','e1'),
              ('a3','b1','c1','d1','e1')},
              (A,B,C,D,E))
U = relation('U', 'U',
             {('d1','e1'),
              ('d2','e2')}, 
             (D,E))
#exemple d'auto-jointure avec renommage des attributs
SUCC = relation('SUCC', 'SUCC',
             {(x,x+1) for x in ext}|{(0,0)}, 
             (F,G))
SUCC2 = relation('SUCC2', 'SUCC2',
             {(x,x+1) for x in ext}|{(0,0)}, 
             (G,H))

relations = [R, R&S, R|S, R-S, R*S, R/U,
             R.projection(A,E),
             R.projection(A,E).selection(a1,E),
             (R.projection(D,E))*U,
             R.projection(D,E).jointure(U,D),
             SUCC.jointure(SUCC2,G).projection(F,H).selection(PAIR,H)]

affiche(relations)