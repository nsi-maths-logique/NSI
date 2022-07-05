import pytest
import lambdaCalcul
from lambdaCalcul import *

booleen(True) & booleen(True)

########################
#TESTS SUR LES BOOLEENS#
########################

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (booleen(True),  booleen(True),  True),
    (booleen(False), booleen(True),  False),
    (booleen(True),  booleen(False), False),
    (booleen(False), booleen(False), True),
])
def test_eq(arg1, arg2, resultat):
    assert (arg1 == arg2) is resultat

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (booleen(True),  booleen(True),  False),
    (booleen(False), booleen(True),  True),
    (booleen(True),  booleen(False), True),
    (booleen(False), booleen(False), False),
])
def test_ne(arg1, arg2, resultat):
    assert (arg1 != arg2) is resultat

@pytest.mark.parametrize('arg, resultat', [
    (booleen(True),  booleen(False)),
    (booleen(False), booleen(True)),
])
def test_invert(arg, resultat):
    assert ~arg == resultat

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (booleen(True),  booleen(True),  booleen(True)),
    (booleen(False), booleen(True),  booleen(False)),
    (booleen(True),  booleen(False), booleen(False)),
    (booleen(False), booleen(False), booleen(False)),
])
def test_et(arg1, arg2, resultat):
    assert (arg1 & arg2) == resultat

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (booleen(True),  booleen(True),  booleen(True)),
    (booleen(False), booleen(True),  booleen(True)),
    (booleen(True),  booleen(False), booleen(True)),
    (booleen(False), booleen(False), booleen(False)),
])
def test_ou(arg1, arg2, resultat):
    assert (arg1 | arg2) == resultat

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (booleen(True),  booleen(True),  booleen(False)),
    (booleen(False), booleen(True),  booleen(True)),
    (booleen(True),  booleen(False), booleen(True)),
    (booleen(False), booleen(False), booleen(False)),
])
def test_xor(arg1, arg2, resultat):
    assert (arg1 ^ arg2) == resultat

@pytest.mark.parametrize('data, resultat', [
    (True, 'VRAI'),
    (False, 'FAUX')
])
def test_show(data, resultat):
    assert booleen(data).show() is resultat

#######################
#TESTS SUR LES ENTIERS#
#######################

@pytest.mark.parametrize('data, resultat', [
    (0, booleen(True)),
    (1, booleen(False)),
    (2, booleen(False))
])
def test_estZero(data, resultat):
    assert entiers(data).estZero() == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(False)),
    (1, 0, booleen(True)),
    (0, 0, booleen(True))
])
def test_ge(nb1, nb2, resultat):
    assert (entiers(nb1) >= entiers(nb2)) == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(True)),
    (1, 0, booleen(False)),
    (0, 0, booleen(True))
])
def test_le(nb1, nb2, resultat):
    assert (entiers(nb1) <= entiers(nb2)) == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(False)),
    (1, 0, booleen(True)),
    (0, 0, booleen(False))
])
def test_gt(nb1, nb2, resultat):
    assert (entiers(nb1) > entiers(nb2)) == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(True)),
    (1, 0, booleen(False)),
    (0, 0, booleen(False))
])
def test_lt(nb1, nb2, resultat):
    assert (entiers(nb1) < entiers(nb2)) == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(False)),
    (1, 0, booleen(False)),
    (0, 0, booleen(True))
])
def test_eq(nb1, nb2, resultat):
    assert (entiers(nb1) == entiers(nb2)) == resultat

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, booleen(True)),
    (1, 0, booleen(True)),
    (0, 0, booleen(False))
])
def test_ne(nb1, nb2, resultat):
    assert (entiers(nb1) != entiers(nb2)) == resultat

@pytest.mark.parametrize('nb, resultat', [
    (0, 1),
    (1, 2),
    (2, 3)
])
def test_succ(nb, resultat):
    assert entiers(nb).succ() == entiers(resultat)

@pytest.mark.parametrize('nb, resultat', [
    (0, 0),
    (1, 0),
    (2, 1)
])
def test_pred(nb, resultat):
    assert entiers(nb).pred() == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 1),
    (1, 0, 1),
    (0, 0, 0),
    (1, 1, 2),
    (7, 5, 12)
])
def test_add(nb1, nb2, resultat):
    assert (entiers(nb1) + entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 0),
    (1, 1, 1),
    (7, 3, 21)
])
def test_mult(nb1, nb2, resultat):
    assert (entiers(nb1) * entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 0),
    (1, 1, 0),
    (6, 4, 2)
])
def test_sous(nb1, nb2, resultat):
    assert (entiers(nb1) - entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (1, 1, 1),
    (2, 3, 8)
])
def test_puiss(nb1, nb2, resultat):
    assert (entiers(nb1) ** entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 0),
    (1, 1, 1),
    (2, 3, 2)
])
def test_min(nb1, nb2, resultat):
    assert (entiers(nb1).min(entiers(nb2))) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 1),
    (1, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (2, 3, 3)
])
def test_max(nb1, nb2, resultat):
    assert (entiers(nb1).max(entiers(nb2))) == entiers(resultat)

@pytest.mark.parametrize('nb, resultat', [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24)
])
def test_fact(nb, resultat):
    assert entiers(nb).factorielle() == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 2),
    (4, 2, 2)
])
def test_divEnt(nb1, nb2, resultat):
    assert (entiers(nb1)//entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb1, nb2, resultat', [
    (0, 1, 0),
    (1, 1, 0),
    (1, 2, 1),
    (4, 2, 0),
    (5, 3, 2)
])
def test_mod(nb1, nb2, resultat):
    assert (entiers(nb1)%entiers(nb2)) == entiers(resultat)

@pytest.mark.parametrize('nb, resultat', [
    (0, booleen(True)),
    (1, booleen(False)),
    (2, booleen(True)),
    (3, booleen(False)),
    (4, booleen(True))
])
def test_pair(nb, resultat):
    assert entiers(nb).estPair() == resultat

@pytest.mark.parametrize('nb, resultat', [
    (0, booleen(False)),
    (1, booleen(True)),
    (2, booleen(False)),
    (3, booleen(True)),
    (4, booleen(False))
])
def test_impair(nb, resultat):
    assert entiers(nb).estImpair() == resultat

@pytest.mark.parametrize('nb, resultat', [
    (0, 0),
    (1, 1),
    (99, 99)
])
def test_nbshow(nb, resultat):
    assert entiers(nb).show() == resultat
#######################
#TESTS SUR LES COUPLES#
#######################

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (0, 1, 0),
    (1, 0, 1)
])
def test_cplcar(arg1, arg2, resultat):
    assert couple(entiers(arg1), entiers(arg2)).car() == entiers(resultat)

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (0, 1, 1),
    (1, 0, 0)
])
def test_cplcdr(arg1, arg2, resultat):
    assert couple(entiers(arg1), entiers(arg2)).cdr() == entiers(resultat)

@pytest.mark.parametrize('arg1, arg2, resultat', [
    (0, 1, (0, 1))
])
def test_cplcshow(arg1, arg2, resultat):
    assert couple(entiers(arg1), entiers(arg2)).show() == resultat
######################
#TESTS SUR LES LISTES#
######################
@pytest.mark.parametrize('data, resultat', [
    ([1, 2, True, 'a', 5], [1, 2, 'VRAI', 'a', 5])
])
def test_charge(data, resultat):
    l = liste()
    lPython = data
    l.charge(lPython)   
    assert l.show() == resultat

@pytest.mark.parametrize('data, resultat', [
    ([], liste.VRAI.value),
    ([1], liste.FAUX.value)
])
def test_list_estVide(data, resultat):
    l = liste()
    lPython = data
    l.charge(lPython)
    assert l.estVide() == resultat

@pytest.mark.parametrize('data, resultat', [
    ([1, 2, True, 'a', 5], 1)
])
def test_list_tete(data, resultat):
    l = liste()
    lPython = data
    l.charge(lPython)   
    assert l.tete().show() == resultat

@pytest.mark.parametrize('data, resultat', [
    ([1, 2, True, 'a', 5], [2, 'VRAI', 'a', 5])
])
def test_list_queue(data, resultat):
    l = liste()
    lPython = data
    l.charge(lPython)   
    assert l.queue().show() == resultat

@pytest.mark.parametrize('myliste, data, resultat', [
    ([], 1, [1]),
    ([2], 1, [1,2])
])
def test_list_empile(myliste, data, resultat):
    l = liste()
    lPython = myliste
    l.charge(lPython)     
    assert l.empile(entiers(data)).show() == resultat

@pytest.mark.parametrize('myliste, data, resultat', [
    ([], 1, [1]),
    ([2], 1, [2,1])
])
def test_list_ajoute(myliste, data, resultat):
    l = liste()
    lPython = myliste
    l.charge(lPython)     
    assert l.ajoute(entiers(data)).show() == resultat

@pytest.mark.parametrize('myliste, resultat', [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1])
])
def test_list_inverse(myliste, resultat):
    l = liste()
    lPython = myliste
    l.charge(lPython)     
    assert l.inverse().show() == resultat

@pytest.mark.parametrize('self, other, resultat', [
    ([], [], []),
    ([1], [], [1]),
    ([], [1], [1]),
    ([1, 2, 3], [3, 2, 1], [1, 2, 3, 3, 2, 1])
])
def test_list_concatene(self, other, resultat):
    l1 = liste()
    l1.charge(self)
    l2 = liste()
    l2.charge(other) 
    assert l1.concatene(l2).show() == resultat

@pytest.mark.parametrize('self, resultat', [
    ([], 0),
    ([1], 1),
    ([1,2], 2)
])
def test_list_longueur(self, resultat):
    l = liste()
    l.charge(self)
    assert l.longueur().show() == resultat

