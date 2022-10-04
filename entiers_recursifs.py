'''Definition recursive des entiers'''
import re

#POINT_FIXE = None#Le theoreme de Kleene nous assure qu'il existe, mais inaccessible pour un ordi
POINT_FIXE = 's(s(s(s(s(0)))))'#Intervalle entier [0,5]
#POINT_FIXE = 's(s(s(s(s(s(s(s(s(s(0))))))))))'#Intervalle entier [0,10]

def s(x):
    '''Constructeur natif des entiers'''
    if x == POINT_FIXE:
        return x
    return 's(%s)'%x
  
def succ(X):
    '''Constructeurs natif des definitions recursives'''
    return X | {s(x) for x in X}

def succ_n(n, X):
  '''Pour rechercher manuellement du point fixe de succ'''
  if n == 1:
    return succ(X)
  return succ(succ_n(n-1, X))

def rec_n():
  '''Definition recursive des entiers'''
  D = {'0'}
  REC_N = D#C1 : D ⊆ REC_N
  while REC_N != succ(REC_N):#Theoreme du point fixe de Kleene = condition d'arret
    yield max(REC_N)
    REC_N = succ(REC_N)#C2 : si X ⊆ REC_N alors succ(N) ⊆ REC_N
  yield max(REC_N)
  
def conversion(n):
  '''Fonction de generation d'un entier recursif'''
  m = rec_n()
  for i in range(n):
    next(m)
  return next(m)

def pred(x):
  if x == '0':
    return '0'
  prog = re.compile('^s\((.*)\)$')
  return prog.match(x)[1]
  
def add(x, y):
  if y == '0':
    return x
  return s(add(x, pred(y)))

def mult(x, y):
  if y == '0':
    return y
  return add(x, mult(x, pred(y)))

def pow(x, y):
  if y == '0':
    return 's(0)'
  else:
    return mult(x, pow(x, pred(y)))

def less(x, y):
  if y == '0':
    return x
  else:
    return pred(less(x, pred(y)))

def fact(x):
  if x == 's(0)':
    return 's(0)'
  return mult(x, fact(pred(x)))

if POINT_FIXE != None:
  print('REC_N : ', {x for x in rec_n()})
n2 = conversion(2)
n3 = conversion(3)
print('n2 : ', n2)
print('n3 : ', n3)
print('add(n3, n2) : ', add(n3, n2))
#Attention... si POINT_FIXE == 5 alors renvoie 5 car s(5)=5
print('mult(n3, n2) : ', mult(n3, n2))
#Attention... si POINT_FIXE == 5 alors renvoie 5 car s^4(5)=5
print('pow(n3, n2) : ', pow(n3, n2))
print('less(n3, n2) : ', less(n3, n2))
print('fact(n2) : ', fact(n2))