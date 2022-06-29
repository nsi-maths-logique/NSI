
'''Classe entiersDeZermelo des entiers de Zermelo

        L'element de base de la classe est set() et le constructeur succ(x) defini par {x}

        Les comparateurs implantes sont :

                                        <, <=, >, >=, ==, !=

        Les operateurs implantes sont :

                                         +, -, *, **, //, %

        Pour definir un entier de Zermelo, il faut ecrire :

                                    z10 = entiersDeZermelo(10)

        Pour definir un intervalle [z0, z10] d'entier de von neumann, il est 'possible' d'ecrire :

                for i in range(0,11):
                    globals()['z%d' % i ] = entiersDeZermelo(i)

        !!!Attention, les entiers de Zermelo ont un interet theorique mais pas pratique car leur
        representation est gloutone. Il est conseille de s'en tenir a de petits entiers.!!!
 
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
	         7 + 8   :  15 
        Operateur - :
        -------------
	         8 - 7   :  1   |   0 - 7   :  0  |   7 - 0   :  7 
        Operateur * :
        -------------
	         3 * 3   :  9   |   3 * 0   :  0   |   0 * 3   :  0 
        Operateur ** :
        --------------
	         2 ** 3   :  8   |   3 ** 0   :  1 
        Operateur // :
        --------------
	         3 // 2   :  1   |   0 // 2   :  0 
        Operateur % :
        --------------
	         3 % 2   :  1   |   0 % 2   :  2 
    '''

class entiersDeZermelo:

    def __init__(self, valInit):
        if type(valInit) == int:
            assert type(valInit) == int or type(valInit) == set
            stack = []
            stack.append(frozenset(set()))
            for i in range(0, valInit+1):
                stack.append({frozenset(stack[i])})
            self.value = stack[valInit]
        else:
            self.value = valInit

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        out = False
        stack = other
        while stack != self.__class__(0):
            stack = stack - self.__class__(1)
            if stack == self:
                return True
        return out

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def pred(self):
        if self == self.__class__(0):
            return self
        return self.__class__(max(self.value))

    def succ(self):
        return self.__class__({frozenset(self.value)})

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
        if other == self.__class__(0):
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
            return (x.__add__(self.__class__(1)), y)

    def __floordiv__(self, other):
            return self.divEuclidienne(other)[0]

    def __mod__(self, other):
            return self.divEuclidienne(other)[1]

    def show(self):
        out = 0
        work = self
        while work != self.__class__(0):
            work = work - self.__class__(1)
            out += 1
        return out
