'''Classe entiersDeVonNeumann des entiers de von Neumann

        L'element de base de la classe est set() et le constructeur succ(x) defini par x|{x}

        Les comparateurs implantes sont :

                                        <, <=, >, >=, ==, !=

        Les operateurs implantes sont :

                                         +, -, *, **, //, %

        Pour definir un entier de von Neumann, il faut ecrire :

                                    n10 = entiersDeVonNeumann(10)

        Pour definir un intervalle [n0, n10] d'entier de von neumann, il est 'possible' d'ecrire :

                for i in range(0,11):
                    globals()['n%d' % i ] = entiersDeVonNeumann(i)

        !!!Attention, les entiers de von Neumann ont un interet theorique mais pas pratique car leur
        representation est gloutone. Il est conseille de s'en tenir a de petits entiers.!!!

        Definition extensionnelle :
        ---------------------------
	         0 est  :  set()
	         1 est  :  {0}
	         2 est  :  {0, 1}
	         3 est  :  {0, 1, 2}
	         4 est  :  {0, 1, 2, 3}
	         5 est  :  {0, 1, 2, 3, 4}
	         6 est  :  {0, 1, 2, 3, 4, 5}
	         7 est  :  {0, 1, 2, 3, 4, 5, 6}
	         8 est  :  {0, 1, 2, 3, 4, 5, 6, 7}
	         9 est  :  {0, 1, 2, 3, 4, 5, 6, 7, 8}
	         10 est :  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
        Operateur < :
        -------------
	         8 < 7    :  False   |   8 < 8    :  False   |    8 < 9    :  True 
        Operateur <= :
        --------------
	         8 <= 7   :  False   |   8 <= 8   :  True   |   8 <= 9   :  True 
        Operateur > :
        -------------
	         8 > 7   :  True   |   8 > 8   :  False   |   8 > 9   :  False 
        Operateur >= :
        --------------
	         8 >= 7  :  True   |   8 >= 8  :  True   |   8 >= 9  :  False 
        Operateur == :
        ---------------
	         8 == 7  :  False   |   8 == 8  :  True 

        Operateur != :
        --------------
	         8 != 7  :  True   |   8 != 8  :  False 
        Operateur + :
        -------------
	         7 + 8   :  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14} 
        Operateur - :
        -------------
	         8 - 7   :  {0}   |   0 - 7   :  set()   |   7 - 0   :  {0, 1, 2, 3, 4, 5, 6} 
        Operateur * :
        -------------
	         3 * 3   :  {0, 1, 2, 3, 4, 5, 6, 7, 8}   |   3 * 0   :  set()   |   0 * 3   :  set() 
        Operateur ** :
        --------------
	         2 ** 3   :  {0, 1, 2, 3, 4, 5, 6, 7}   |   3 ** 0   :  {0} 
        Operateur // :
        --------------
	         3 // 2   :  {0}   |   0 // 2   :  set() 
    '''

class entiersDeVonNeumann:

    def __init__(self, valInit):
        if type(valInit) == int:
            assert type(valInit) == int or type(valInit) == set
            stack = []
            stack.append(frozenset(set()))
            for i in range(0, valInit+1):
                stack.append(stack[i]|{stack[i]})
            self.value = stack[valInit]
        else:
            self.value = valInit

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value.issubset(other.value) and self != other

    def __le__(self, other):
        return self.value.issubset(other.value)

    def __gt__(self, other):
        return other.value.issubset(self.value) and self != other

    def __ge__(self, other):
        return other.value.issubset(self.value)

    def pred(self):
        if self == self.__class__(0):
            return self
        return self.__class__(max(self.value))

    def succ(self):
        return self.__class__(self.value|{self.value})

    def __add__(self, other):
        if other == self.__class__(0):
            return self
        else:
            return self.__add__(other.pred()).succ()
    
    def __sub__(self, other):
        if other == self.__class__(0):
            return self
        else:
            return self.__sub__(other.pred()).pred()

    def __mul__(self, other):
        if other.lue == self.__class__(0):
            return self.__class__(0)
        else:
            return self.__add__(self.__mul__(other.pred()))

    def __pow__(self, other):
        if other == self.__class__(0):
            return self.__class__(1)
        else:
            return self.__mul__(self.__pow__(other.pred()))

    def divEuclidienne(self, other):
        assert other != self.__class__(0), 'Ooops : Division by zero is not allowed'
        if self < other:
            return (self.__class__(0), self)
        else:
            x, y = self.__sub__(other).divEuclidienne(other)
            return (x + self.__class__(1), y)

    def __floordiv__(self, other):
            return self.divEuclidienne(other)[0]

    def __mod__(self, other):
            return self.divEuclidienne(other)[1]

    def show(self):
        out = set()
        work = set(self.value)
        i = 0
        while work != frozenset(set()):
            n = self.__class__(i)
            work.remove(n.value)
            out.add(i)
            i += 1
        return out

