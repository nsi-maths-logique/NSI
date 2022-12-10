from booleen import *
from entiers import *
#fonctions
#λn.λf.λx.f (n f x)
SUCC    = lambda n: lambda f: lambda x: f(n(f)(x))
PLUS    = lambda a: lambda b: a(SUCC)(b)
MUL     = lambda a: lambda b: lambda c: a(b(c))
PUIS    = lambda a: lambda b: b(a)
PRED    = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(lambda a: a)
MOINS   = lambda a: lambda b: b(PRED)(a)
DIFF    = lambda a: lambda b: PLUS(MOINS(a)(b))(MOINS(b)(a))
#TESTS
ESTZERO = lambda a: a(lambda _: FAUX)(VRAI)
PGE     = lambda a: lambda b: ESTZERO(MOINS(b)(a))
PPE     = lambda a: lambda b: ESTZERO(MOINS(a)(b))
PG      = lambda a: lambda b: ESTZERO(MOINS(SUCC(b))(a))
PP      = lambda a: lambda b: ESTZERO(MOINS(SUCC(a))(b))
EG      = lambda a: lambda b: ET(PGE(a)(b))(PPE(a)(b))
#ARITHMETIQUE
MIN     = lambda a: lambda b: PPE(a)(b)(a)(b)
MAX     = lambda a: lambda b: PGE(a)(b)(a)(b)
#COMBINATEUR
Z       = lambda f: ((lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y))))
#ARITHMETIQUE AVEC PT FIXE
FAC     = Z(
  lambda f: lambda n: ESTZERO(n)
  (lambda _: UN)
  (lambda _: MUL(n)(f(PRED(n))))
  (ZERO)
)
FIB     = Z(
    lambda f: lambda n: PPE(n)(DEUX)
    (lambda _: UN)
    (lambda _: PLUS(f(PRED(n)))(f(PRED(PRED(n)))))
    (ZERO)
)
DIV     = Z(
  lambda f: lambda a: lambda b: PP(a)(b)
  (lambda _: ZERO)
  (lambda _: SUCC(f(MOINS(a)(b))(b)))
  (ZERO)
)
MOD     = Z(
  lambda f: lambda a: lambda b: PP(a)(b)
  (lambda _: a)
  (lambda _: f(MOINS(a)(b))(b))
  (ZERO)
)
PAIR    = lambda a: ESTZERO(MOD(a)(DEUX))
IMPAIR  = lambda a: NON(PAIR(a))
