from booleen import *

CONS    = lambda a: lambda b: lambda c: c(a)(b)
CAR     = lambda p: p(VRAI)
CDR     = lambda p: p(FAUX)
NULL    = lambda _: VRAI
ISNULL  = lambda _: lambda _: FAUX
