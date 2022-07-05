'''Module destine aux eleves de Terminale avec option NSI pour introduire la programmation fonctionnelle
Implantation des booleens :
    - Vrai : λa.λb.a
    - Faux : λa.λb.b
    - Negation (~) : λa.a(Faux)(Vrai)
    - Conjonction (&) : λa.λb.a(b)(Faux)
    - Disjonction (|) : λa.λb.a(b)(Vrai)
    - Disjonction exclusive (^) : λa.λb.a(b(Faux)(Vrai))(b(Vrai)(Faux))
Implantation des combinateurs :
    - I : λa.a
    - K : λa.λb.a
    - S : λa.λb.λc.a(c)(b(c))
    - Y : λf.((λx.f(λy.x(x)(y)))(λx.f(λy.x(x)(y))))
Implantation des entiers de Church
    - 0 : λa.λb.b
    - 1 : λa.λb.a
    - Fonction estZero : λa.a(Faux)(Vrai)
    - >= : λa.λb.(estZero)(Soustraction)(b)(a)
    - <= : λa.λb.(estZero)(Soustraction)(a)(b)
    - > : λa.λb.(estZero)(Soustraction)((Successeur)b)(a)
    - < : λa.λb.(estZero)(Soustraction)((Successeur)a)(b)
    - == : λa.λb.(a >= b) & (b <= a)
    - != : λa.λb.(a < b) | (b > a)
    - Successeur (succ) : λn.λs.λz.s(n(s)(z))
    - Predecesseur (pred) : λn.λs.λz.n(λg.λh.h(g(s)))(λb.z)(λa.a)
    - Addition (+) : λn.λm.(n)(Successeur)(m)
    - Soustraction (-) : λn.λm.(m)(Predecesseur)(n)
    - Multiplication (*) : λn.λm.λc.(n)((m)(c))
    - Puissance (**) : λn.λm.(n)(m)
    - Division entiere (//) :Y(λf.λa.λb.λc.(a < b)(λ_.c)(λ_.f(a - b)(b)((SUCC(c)))
    - Modulo (%) : Y(λf.λa.λb.(a < b)(λ_.a)(λ_.f(a - b)(b))(Zero))
    - Fonction min : λn.λm.(n <= m)(n)(m)
    - Fonction max : λn.λm.(n >= m)(n)(m)
    - Fonction factorielle : Y(λf.λn.estZero(n)(λ_.1)(λ_.n * f((PRED)n))(Zero))
    - Predicat estPair : λn.estZero(n % 2)
    - Predicat estImpair : λn.~estPair(n)
Implantation des couples : [cons = λn.λm.λf.f(n)(m)]
    - Fonction car : λf.f(Vrai)
    - Fonction cdr : λf.f(Faux)
Implantation des listes : [liste vide (nil)= (vrai,vrai)][liste non vide = (faux,...,vrai)]
    - Fonction estVide  :  λl.car(l)
    - Fonction tete :  λl.cdr((car)l)
    - Fonction queue :  λl.cdr((cdr)l)
    - Fonction empile : λl.λa.cons(Faux)cons(a)(l)
    - Fonction ajoute : Y(λf.λl.λx.estVide(l)(λ_.empile(l)(x))(λ_.cons(Faux)cons(tete(l))(f(queue(l))(x)))(Vrai))
    - Fonction inverse : Y(λf.λl.estVide(l)(λ_.nil)(λ_.(Ajoute)(f(queue(l)))(tete(l)))(Vrai))
    - Fonction concatene : Y(λf.λl1.λl2.estVide(l2)(λ_.l1)(λ_.f(ajoute(l1)(tete(l2)))(queue(l2)))(Vrai))
    - Fonction longueur :Y(λf.λl.λn.estVide(l)(λ_.n)(λ_.f(queue(l))(succ(n)))(Vrai))
'''
class booleen():
    VRAI = lambda a: lambda b: a
    FAUX = lambda a: lambda b: b
    def __init__(self, valeur):
        if valeur == True:
            self.value = __class__.VRAI
        elif valeur == False:
            self.value = __class__.FAUX
        else:
            self.value = valeur
    def __eq__(self, other):#==
        return self.value == other.value
    def __ne__(self, other):#!=
        return self.value != other.value
    def __invert__(self):#~
        return self.__class__((lambda a: a(__class__.FAUX)(__class__.VRAI))(self.value))
    def __and__(self, other):#&
        return self.__class__((lambda a: lambda b: a(b)(__class__.FAUX))(self.value)(other.value))
    def __or__(self, other):#|
        return self.__class__((lambda a: lambda b: a(__class__.VRAI)(b))(self.value)(other.value))
    def __xor__(self, other):#^
        return self.__class__((lambda a: lambda b: a(b(__class__.FAUX)(__class__.VRAI))(b(__class__.VRAI)(__class__.FAUX)))(self.value)(other.value))
    def show(self):
        if self.value == __class__.VRAI:
            return 'VRAI'
        elif self.value == __class__.FAUX:
            return 'FAUX'

class combinateur():
    def __init__(self, valeur):
        if valeur == 'I':
            self.value = lambda a: a
        elif valeur == 'K':
            self.value = lambda a: lambda b: a
        elif valeur == 'S':
            self.value = lambda a: lambda b: lambda c: a(c)(b(c))
        elif valeur == 'Y':
            self.value = lambda f: ((lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y))))

class entiers():
    SUCC = lambda n: lambda s: lambda z: s(n(s)(z))
    PRED = lambda n: lambda s: lambda z: n(lambda g: lambda h: h(g(s)))(lambda _: z)(lambda a: a)
    def __init__(self, valeur):
        if type(valeur) == int:
            self.value = lambda s: lambda z: z
            for i in range(0, valeur):
                self.value = (__class__.SUCC)(self.value)
        else:
            self.value = valeur
    def estZero(self):
        return booleen((self.value)(lambda _: booleen.FAUX)(booleen.VRAI))
    def __ge__(self, other):#>=
        return (other - self).estZero()    
    def __le__(self, other):#<=
        return (self - other).estZero()
    def __gt__(self, other):#>
        return (other.succ() - self).estZero()
    def __lt__(self, other):#<
         return (self.succ() - other).estZero()
    def __eq__(self, other):#==
        return (self >= other) & (self <= other)
    def __ne__(self, other):#!=
        return (self > other) | (self < other)
    def succ(self):
        return self.__class__((__class__.SUCC)(self.value))
    def pred(self):
        return self.__class__((__class__.PRED)(self.value))
    def __add__(self, other):#+
        return self.__class__((self.value)(__class__.SUCC)(other.value))
    def __mul__(self, other):#*
        return self.__class__(lambda c: (self.value)((other.value)(c)))
    def __sub__(self, other):#-
        return self.__class__((other.value)(__class__.PRED)(self.value))
    def __pow__(self, other):#**
        return self.__class__((other.value)(self.value))
    def min(self, other):
        return self.__class__(((self <= other).value)(self.value)(other.value))
    def max(self, other):
        return self.__class__(((self >= other).value)(self.value)(other.value))
    def factorielle(self):
        '''Y boucle sur n (le parametre de f) en le decrementant jusqu'a ce qu'il soit egal a 0'''
        Y = combinateur('Y').value
        out = Y(lambda f: lambda n: n.estZero().value
                    (lambda _: __class__(1))
                    (lambda _: n * f(n.pred()))
                    (__class__(0).value)
                )(self)
        return out
    def __floordiv__(self, other):#//
        '''Y boucle sur a, b (les 2 premiers parametre de f) en soustrayant b de a tant que a!=0, on compte le nombre de passage avec c'''
        assert other.show() != 0, "Ooops, le deuxieme argument ne peut pas etre 0"
        Y = combinateur('Y').value
        out = Y(lambda f: lambda n: lambda m: lambda res: (n < m).value
                    (lambda _: res)
                    (lambda _: f(n - m)(m)(res.succ()))
                    (__class__(0).value)
                )(self)(other)(entiers(0))
        return out
    def __mod__(self, other):#%
        '''On boucle sur a en enlevant b a chaque tour, quand a < b on retourne le reste'''
        assert other.show() != 0, "Ooops, le deuxieme argument ne peut pas etre 0"
        Y = combinateur('Y').value
        out = Y(    lambda f: lambda n: lambda m: (n < m).value
                    (lambda _: n)
                    (lambda _: f(n - m)(m))
                    (__class__(0).value)
                )(self)(other)
        return out
    def estPair(self):
        return (self % self.__class__(2)).estZero()
    def estImpair(self):
        return ~ self.estPair()
    def show(self)-> int:
        return (self.value)(lambda x: x + 1)(0)

class caractere():
    def __init__(self, valeur):
        self.value = valeur
    def show(self):
        return self.value

class couple():
    def __init__(self, valeur1, valeur2):
        self.value = lambda f: f(valeur1)(valeur2)
    def car(self):
        return (lambda f: f(booleen(True).value))(self.value)
    def cdr(self):
        return (lambda f: f(booleen(False).value))(self.value) 
    def show(self):
        try:
            self.car().car()
            try:
                self.cdr().car()
                return (self.car().show(), self.cdr().show())
            except:
                return (self.car().show(), self.cdr())
        except:
            try:
                self.cdr().car()
                return (self.car().show(), self.cdr().show())
            except:
                return (self.car().show(), self.cdr().show())

class liste():
    VRAI = booleen(True)
    FAUX = booleen(False)
    NULL = lambda _: VRAI.value
    def __init__(self, *list):
        if len(list) == 0:
            self.value = couple(__class__.VRAI.value, __class__.VRAI.value)
        else:
            self.value = list[0]
    def charge(self, listeDonnee):
        '''Charge une liste Python donnee contenant des int, bool, str dans une liste du lamba-calcul'''
        out = __class__()
        for elem in listeDonnee:
            assert type(elem) == int or type(elem) == str or type(elem) == bool, "Ooops, les membres de la liste doivent etre des entiers, des booleens ou des caracteres"
            if type(elem) == int:
                out = out.ajoute(entiers(elem))
            elif type(elem) == bool:
                out = out.ajoute(booleen(elem))
            elif type(elem) == str:
                out = out.ajoute(caractere(elem))
        self.value = out.value
    def estVide(self):
        return self.value.car()
    def tete(self):
        return self.value.cdr().car()
    def queue(self):
        return self.__class__(self.value.cdr().cdr())
    def queueCouple(self):
        return self.value.cdr().cdr()
    def empile(self, valeur):
        return self.__class__(couple(__class__.FAUX.value, couple(valeur, self.value)))
    def empileCouple(self, valeur):
        return couple(__class__.FAUX.value, couple(valeur, self.value))
    def ajoute(self, valeur):
        '''On boucle sur la liste jusqu'a atteindre la fin et on ajoute x'''
        assert type(valeur) == entiers or type(valeur) == booleen or type(valeur) == caractere
        Y = combinateur('Y').value
        out= Y(
                    lambda f: lambda l: lambda x: (l.estVide())
                    (lambda _: l.empileCouple(x))
                    (lambda _: couple(__class__.FAUX.value, couple(l.tete(), f(l.queue())(x))))
                    (__class__.VRAI.value)
                )(self)(valeur)
        return self.__class__(out)
    def inverse(self):
        '''On boucle sur la liste jusqu'a atteindre la fin en accumulant la tete de la queue'''
        Y = combinateur('Y').value
        out= Y(
                    lambda f: lambda l: (l.estVide())
                    (lambda _: self.__class__())
                    (lambda _: f(l.queue()).ajoute(l.tete()))
                    (__class__.VRAI.value)
                )(self)
        return out
    def concatene(self, other):
        '''On boucle sur la liste 2 en ajoutant la tete a la liste 1, en fin de liste on renvoie la liste 1'''
        Y = combinateur('Y').value
        out= Y(
                    lambda f: lambda l1: lambda l2: (l2.estVide())
                    (lambda _: l1)
                    (lambda _: f(l1.ajoute(l2.tete()))(l2.queue()))
                    (__class__.VRAI.value)
                )(self)(other)
        return out
    def longueur(self):
        '''On parcourt la liste et on incremente n a chaque passage pour renvoyer en fin de liste'''
        Y = combinateur('Y').value
        out= Y(
                    lambda f: lambda l: lambda n: (l.estVide())
                    (lambda _: n)
                    (lambda _: f(l.queue())(n.succ()))
                    (__class__.VRAI.value)
                )(self)(entiers(0))
        return out
    def show(self):
        out = []
        for _ in range(100):
            if self.estVide() == __class__.VRAI.value:
                return out
            else:
                out.append(self.tete().show())
            self = self.queue()
        raise RuntimeError('Probablement une liste infinie...')