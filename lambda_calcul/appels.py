import lambda_calcul
from lambda_calcul import *

b = booleen(True)
print('b.show() -> ', b.show())

dix = entiers(10)
cinq = entiers(5)
deux = entiers(2)
print('dix.show() -> ', dix.show())
print('(cinq * cinq).show() -> ', (cinq * cinq).show())

a = caractere('a')
b = caractere('b')
ab = couple(a, b)
print('ab.show() -> ', ab.show())
print('ab.car().show() -> ', ab.car().show())

l1 = liste()
l1.charge([1,2,3])
l2 = liste()
l2.charge([4,5,6])
print('l1.concatene(l2).show() -> ',l1.concatene(l2).show())
print('l1.concatene(l2).inverse().show() -> ', l1.concatene(l2).inverse().show())
print('l1.concatene(l2).inverse().longueur().show() -> ', l1.concatene(l2).inverse().longueur().show())