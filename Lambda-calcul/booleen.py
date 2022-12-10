FAUX    = lambda a: lambda b: b
VRAI    = lambda a:lambda b: a
NON     = lambda a: a (FAUX) (VRAI)
ET      = lambda a:lambda b: a (b) (FAUX)
OU      = lambda a:lambda b: a (VRAI) (b)
XOR     = lambda a:lambda b: (b (FAUX) (VRAI))(b (VRAI) (FAUX))
ITE     = lambda c:lambda a:lambda b:c (a) (b)

