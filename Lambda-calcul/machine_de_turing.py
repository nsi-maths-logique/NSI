import sys
sys.setrecursionlimit(10**6)
from listes import *

#On implante le ruban via deux listes
#La tete de lecture est situee en tete de la seconde liste
# [e1,...,en][en+1,...en+m]
#               ↑

# [e1,...,en-1][en,en+1,...en+m]
#               ↑
DROITE_1    = lambda g:lambda d: EMPTY(d)(g)(PREPEND(g)(HEAD(d)))
DROITE_2    = lambda d: TAIL(d)
# [e1,...,en,en+1][en+2,...en+m]
#                   ↑    
GAUCHE_1    = lambda g: REVERSE(TAIL(REVERSE(g)))
GAUCHE_2    = lambda g:lambda d: PREPEND(d)(HEAD(REVERSE(g)))
#On renvoie le premier element de la seconde liste
LIT         = lambda l: EMPTY(l)(LIST)(HEAD(l))
#On remplace le premier element de la seconde liste
ECRIT       = lambda e:lambda l: PREPEND(TAIL(l))(e)
#On fusionne les deux listes
FIN         = lambda g:lambda d: CONCAT(g)(d)
# On charge le programme p et on l'applique sur la donnee l
TURING      = lambda p:lambda l: p (l)

#PROGRAMME DU CALCUL DU SUCCESSEUR SUR UN NOMBRE DE BITS DETERMINE

###############################
# TABLE DE TRANSITION #########
###############################

#ETAT 2
INC2 = Z(
    lambda f:lambda l1:lambda l2:lambda e: (
        ESTZERO(e)
        #Si le caractere lu est O, on le remplace par 1 et on revoie les deux listes
        ( lambda _: FIN (l1) (ECRIT(UN)(l2)) )
        #Tant que le caractere lu est 1, on le remplace par 0 et on va a gauche
        ( lambda _: f (GAUCHE_1(l1)) (GAUCHE_2(l1)(ECRIT(ZERO)(l2))) (LIT(GAUCHE_2(l1)(ECRIT(ZERO)(l2)))) )    
        (VRAI)
))
#ETAT 1
INC1 = Z(
    lambda f:lambda l1:lambda l2:lambda e: (
        EMPTY(e)
        #Si on est en fin de liste on passe en etat 2
        ( lambda _: INC2 (GAUCHE_1(l1)) (GAUCHE_2(l1)(l2)) (LIT(GAUCHE_2(l1)(l2))) )
        #Tant qu'on est pas sur la fin de liste, on va a droite
        ( lambda _: f (DROITE_1(l1)(l2)) (DROITE_2(l2)) (LIT(DROITE_2(l2))) )
        (VRAI)
))

#On simule deux listes a partir de notre liste initiale
INC = lambda l: INC1(l) (LIST) (LIST)

data = APPEND(APPEND(APPEND(APPEND(APPEND(LIST)(ZERO))(ZERO))(ZERO))(ZERO))(ZERO)
print(decode_list(data))
for i in range(31):
    data = TURING(INC)(data)
    print(decode_list(data))





