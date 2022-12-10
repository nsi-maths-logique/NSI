from booleen import *
from entiers import *
from arithmetique import *
from couples import *

LIST    = CONS(VRAI)(VRAI)
PREPEND = lambda l: lambda e: CONS(FAUX)(CONS(e)(l))
EMPTY   = lambda l: CAR(l)
HEAD    = lambda l: CAR(CDR(l))
TAIL    = lambda l: EMPTY(l)(l)(CDR(CDR(l)))
APPEND  = Z(
    lambda f: lambda xs: lambda x: EMPTY(xs)
    (lambda _: PREPEND(xs)(x))
    (lambda _: CONS(FAUX)(CONS(HEAD(xs))(f(TAIL(xs))(x))))
    (VRAI)
)
REVERSE = Z(
    lambda f: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: APPEND(f(TAIL(xs)))(HEAD(xs)))
    (VRAI)
)
CONCAT = Z(
    lambda f: lambda l1: lambda l2: EMPTY(l2)
    (lambda _: l1)
    (lambda _: f(APPEND(l1)(HEAD(l2)))(TAIL(l2)))
    (VRAI)
)
MAP = Z(
    lambda f: lambda a: lambda xs: EMPTY(xs)
    (lambda _: LIST)
    (lambda _: PREPEND(f(a)(TAIL(xs)))(a(HEAD(xs))))
    (VRAI)
)
RANGE = Z(
    lambda f: lambda a: lambda b: PGE(a)(b)
    (lambda _: LIST)
    (lambda _: PREPEND(f(SUCC(a))(b))(a))
    (VRAI)
)
REDUCE = FOLD = Z(
    lambda f: lambda r: lambda l: lambda v: EMPTY(l)
    (lambda _: v)
    (lambda _: f(r)(TAIL(l))(r(HEAD(l))(v)))
    (VRAI)
)
FILTER = lambda f: lambda l: (
    REDUCE
    (lambda x: lambda xs: f(x)(APPEND(xs)(x))(xs))
    (l)
    (LIST)
)
DROP = lambda n: lambda l: n(TAIL)(l)
TAKE = Z(lambda f: lambda n: lambda l: (
    OU(EMPTY(l))(ESTZERO(n))
    (lambda _: LIST)
    (lambda _: (
        PREPEND(f(PRED(n))(TAIL(l)))
        (HEAD(l))
    ))
    (VRAI)
))
LENGTH = lambda l: REDUCE(lambda x: lambda n: SUCC(n))(l)(ZERO)
INDEX = Z(lambda f: lambda n: lambda l: (
    ESTZERO(n)
    (lambda _: HEAD(l))
    (lambda _: f(PRED(n))(TAIL(l)))
    (VRAI)
))
ANY = Z(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: FAUX)
    (lambda _: HEAD(l)(VRAI)(f(TAIL(l))))
    (VRAI)
))
ALL = Z(lambda f: lambda l: (
    EMPTY(l)
    (lambda _: VRAI)
    (lambda _: NON(HEAD(l))(FAUX)(f(TAIL(l))))
    (VRAI)
))
def decode_list(encoded):
    decoded = []
    for _ in range(10000):
        if EMPTY(encoded) is VRAI:
            return decoded
        decoded.append(int(HEAD(encoded) == UN))
        encoded = TAIL(encoded)
    raise RuntimeError('probably infinite list')