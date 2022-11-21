class attribut:
    '''
    Simule un type sous forme d'un ensemble de valeurs

    L'argument subset permet de definir un sous-type dont la definition en extension sera visible au lieu du nom
    '''
    def __init__(self, name, value, subset = False):
        if subset:
            self.name = str(value)
            self.subset = subset
        else:
            self.name = name
        self.value = value

class relation:
    '''
    Simule une table de base de donnee sur la base de tuples

    name est le nom de la table
    formule est la formule du premier ordre qui exprime la table
    value est l'ensemble des enregistrements, ce sont des tuples composes selon la signature
    attributs est la signature, c'est un tuple d'attributs
    args est l'ensemble des arguments de la relation/formule qui apparait dans la formule du premier ordre
    arguments est l'ensemble des arguments du nom de la formule
    '''
    def __init__(self, name, formule, value, attributs, arguments = None):
        assert eval(' & '.join(list(map(lambda x: str(isinstance(x, attribut)), attributs)))), "Les attributs doivent etre de type attribut"
        self.attributs = attributs
        self.value = value
        self.name = name
        self.args = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
        self.formule = formule
        if arguments == None:
            self.arguments = self.args
        else:
            self.arguments = arguments
        flag = True
        for i, elem in enumerate(value):
            assert len(elem) == len(attributs), "L'enregistrement %s ne respecte pas la signature de %s"%(str(elem),self.name)
            for j, item in enumerate(elem):
                flag &= item in self.attributs[j].value
                assert flag, "L'element %s de la relation %s ne fait pas partie de l'attribut %s"%(item, self.name, self.attributs[j].name)
    def traduction(self, args = None):
        if args == None:
            args = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
            self.args = args
        self.args = args
        if '(' not in self.formule:
            self.arguments = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
            out = self.formule + '(' + args + ')'
        else:
            out = self.formule
        return out
    def __eq__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        return self.value == other.value
    def __ne__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        return not self.value == other.value
    def __len__(self):
        return len(max(self.value))
    def __and__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        assert self.attributs == other.attributs, "L'intersection s'applique a des relations de meme signature"
        return relation('[%s∩%s]'%(self.name,other.name),"(%s ∧ %s)"%(self.traduction(), other.traduction()),{x for x in self.value if x in other.value},self.attributs)
    def __or__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        assert self.attributs == other.attributs, "L'union s'applique a des relations de meme signature"
        return relation('[%s∪%s]'%(self.name,other.name),"(%s ∨ %s)"%(self.traduction(), other.traduction()),{x for x in self.value}|{x for x in other.value},self.attributs)
    def __sub__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        assert self.attributs == other.attributs, "La difference s'applique a des relations de meme signature"
        return relation('[%s-%s]'%(self.name,other.name),"(%s ∧ ¬%s)"%(self.traduction(), other.traduction()),{x for x in self.value if x not in other.value},self.attributs)
    def __mul__(self, other):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        args1 = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
        max_set = int(max(list(map(lambda x: x[-1], str(self.arguments).split(',')))))
        other.arguments = ','.join(list(map(lambda x: 'x' + str(x),range(max_set+1,max_set+len(other)+1))))
        arguments = ','.join(list(sorted(set(str(self.arguments).split(',') + str(other.arguments).split(',')))))
        return relation('[%s×%s]'%(self.name,other.name),"(%s ∧ %s)"%(self.traduction(args1), other.traduction(other.arguments)),{x+y for x in self.value for y in other.value},self.attributs+other.attributs, arguments)
    def __truediv__(self, other):
        assert isinstance(other, relation), "La division ne s'applique qu'a des relations"
        assert other.attributs == self.attributs[-len(other.attributs):], "%s doit etre un segment final de %s"%(other.name,self.name)
        dim = len(self) - len(other)
        quantificateurs = ''
        for i in range(len(other)+1,len(self)):
            quantificateurs += "∀x%s"%i
        args = ','.join(list(map(lambda x: 'x' + str(x),range(len(other)+1,len(self)))))
        return relation('[%s/%s]'%(self.name,other.name),"%s(%s ⇒ %s)"%(quantificateurs,other.traduction(args),self.traduction()), {x[:dim] for x in self.value if all(x[:dim]+y in self.value for y in other.value)},self.attributs[0:dim])
    def projection(self, *attributs):
        assert set(attributs).issubset(set(self.attributs)), "Vous essayez de faire une projection sur un attribut qui n'existe pas dans %s"%self.name
        out = []
        mesattr = list(map(lambda x: x.name, self.attributs))
        quantificateur = []
        for i, elem in enumerate(mesattr):
            if elem not in {x.name for x in attributs}:
                quantificateur.append(i)
        mesattr.reverse()
        for elem in {x.name for x in self.attributs if x not in attributs}:
            mesattr.remove(elem)
        mesattr.reverse()
        for tuples in self.value:
            mytuple = ()
            arg = []
            for i, item in enumerate(tuples):            
                for attr in attributs:
                    assert isinstance(attr, attribut), "L'element %s doit etre un attribut"%attr
                    if self.attributs[i] == attr:
                        mytuple = mytuple + (item,)
                        arg.append(i)
            quantificateurs = "".join(list(map(lambda x: '∃x' + str(x),quantificateur)))
            out.append(mytuple)
        args = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
        arguments = self.arguments.split(',')
        for elem in quantificateur:
            arguments.remove('x' + str(elem))
        arguments = ','.join(arguments)
        #self.attributs = tuple(mesattr)
        return relation('[%s.π(%s)]'%(self.name,",".join(list(map(lambda x: x.name, attributs)))),quantificateurs + self.traduction(args), set(out), attributs, arguments)
    def selection(self, *attributs):
        assert len(self.attributs) == len(attributs), "Vous devez preciser un attribut pour chaque attribut de %s"%self.name
        diff = []
        for i, elem in enumerate(self.attributs):
            if self.attributs[i] != attributs[i]:
                diff.append(i)
        condition = set()
        for i, elem in enumerate(self.attributs):
            if elem not in attributs:
                condition.add((i, attributs[i]))
        conds = []
        while condition != set():
            elem = condition.pop()
            for item in elem[1].value:
                conds.append('x%d = %s'%(elem[0], item))
        out = {x for x in self.value if all(i for i in diff if x[i] not in attributs[i].value)}
        conditions = ' ∨ '.join(conds)
        return relation('[%s.σ(%s)]'%(self.name,",".join(list(map(lambda x: x.name, attributs)))), "(%s ∧ (%s))"%(self.traduction(), conditions), set(out), attributs, self.arguments)
    def jointure(self, other, *attributs):
        assert isinstance(other, relation), "L'element %s n'est pas une relation"%other
        assert set(attributs).issubset(set(self.attributs)), "Voue essayez de faire une jointure sur un attribut qui n'existe pas dans %s"%self.name
        assert set(attributs).issubset(set(other.attributs)), "Voue essayez de faire une jointure sur un attribut qui n'existe pas dans %s"%other.name
        #calcul de la formule
        argument1 = {}
        argument2 = {}
        max_set = int(max(list(map(lambda x: x[-1], str(self.arguments).split(',')))))
        for i, elem in enumerate(self.attributs):
            argument1[elem.name] = self.arguments.split(',')[i]
        for i, elem in enumerate(other.attributs):
            for item in attributs:
                if elem == item:
                    argument2[elem.name] = argument1[elem.name]
                else:
                    max_set+=1
                    argument2[elem.name] = 'x' + str(max_set)
        args = ','.join(list(map(lambda x: 'x' + str(x),range(len(self)))))
        arg2 = ''
        for elem in argument2:
            arg2 += argument2[elem] + ","
        arg2 = arg2[:-1]
        arguments = ','.join(list(sorted(set(str(self.arguments).split(',') + str(arg2).split(',')))))
        #calcul de la relation
        join = ""
        for attr in attributs:
            selfi = -1
            otheri = -1
            for i, item in enumerate(self.attributs):
                if attr == self.attributs[i]:
                    selfi = i
            for i, item in enumerate(other.attributs):
                if attr == other.attributs[i]:
                    otheri = i
            assert otheri != -1, "L'attribut %s n'est pas attribut de %s"%(attr.name, other.name)
            if selfi != -1 and otheri != -1:
                join += "x[%d] == y[%d] and "%(selfi,otheri)
        join = join[0:-5]
        requete = {x+y for x in self.value for y in other.value if (eval(str(join)))}       
        sortie = set()
        t1 = list(range(len(self)))
        t2 = list(range(len(other)))
        for i, elem in enumerate(other.attributs):
            if elem in attributs:
                t2.remove(i)
        t2 = list(map(lambda x: x + len(self), t2))
        signature = t1+t2
        for tuples in requete:
            sortie.add(tuple(map(lambda x: tuples[x],signature)))
        l = list(other.attributs)
        for elem in attributs:
            l.remove(elem)
        myattributs = self.attributs + tuple(l)
        return relation('[%s⨝(%s)%s]'%(self.name,','.join(map(lambda x: x.name,attributs)),other.name),"(%s ∧ %s)"%(self.traduction(args), other.traduction(arg2)),sortie,myattributs,arguments)
    def __str__(self):
        return '{\n\t' + ",\n\t".join(list(map(lambda x: str(x), self.value))) + '\n}'