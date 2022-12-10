def sn(n, x):
  if n == 0:
    return x
  return f's({sn(n-1,x)})'

def defini_church(n):
  return eval(f"lambda s:lambda z: {sn(n,'z')}")

def genere_church():
  i = -1
  while True:
    i += 1
    yield defini_church(i)

def decode_nombre(f):
    succ = lambda x: x + 1
    return f(succ)(0)

entiers = genere_church()

ZERO    = next(entiers)
UN      = next(entiers)
DEUX    = next(entiers)
TROIS   = next(entiers)
QUATRE  = next(entiers)
CINQ    = next(entiers)
SIX     = next(entiers)
SEPT    = next(entiers)
HUIT    = next(entiers)
NEUF    = next(entiers)
DIX     = next(entiers)
