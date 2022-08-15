import regex
from regex import *

def str_f(*args):
    return args[0][0] + args[0][1] + args[0][2] + args[0][3] + args[0][4] + args[0][5]
def str_g(*args):
    return args[0][0] * 2
def str_h(*args):
    return args[0][1] + args[0][0]
str_c1 = 'a'
str_c2 = 'b'
str_c3 = 'a'

int_f = str_f
int_g = str_g
int_h = str_h
int_c1 = 1
int_c2 = 2
int_c3 = 3

class interpretation:
    def __init__(self, f, g, h, c1, c2, c3):
        self.f = f
        self.g = g
        self.h = h
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3


class term:
    def __init__(self, val, inter = None):
        result = regex.match(r"([cde]\d*|[xyz]\d*|[fgh]\d*\((,?(?R))*\))", val)
        if not result.group(0) == val:
            raise Exception("Ooops, " + val + " n'est pas un terme.")
        self.value = val
        self.name, self.type = self.get_type()
        self.args = []
        if self.type == 'fonction':
            self.arite = self.get_arite(self.value, 0)
            self.get_args()
        else:
            self.arite = 1
    def get_arite(self, text, count):
        if text == '':
            return count;
        const = "^[cde]\d*$|^[cde]\d*,(.*)$"
        var = "^[xyz]\d*$|^[xyz]\d*,(.*)$"
        fonc = "^[fgh]\d*\(.*\)$"
        if regex.match(r"%s" %const, text):
            return self.get_arite(regex.findall(r"%s" %const, text)[0], count + 1)
        elif regex.match(r"%s" %var, text):
            return self.get_arite(regex.findall(r"%s" %var, text)[0], count + 1)
        elif regex.match(r"%s" %fonc, text):
            nb_par_ouv = 0
            nb_par_fer = 0
            i = 0
            while text[i] != '(' and text[i] != ')':
                i += 1
            for j in range(i,len(text)):
                if text[j] == '(':
                    nb_par_ouv += 1
                if text[j] == ')':
                    nb_par_fer += 1
                if nb_par_ouv == nb_par_fer:
                    break
            return self.get_arite(text[i+j+1:], count + 1)
        return
    def get_args(self):
        reg = []
        for i in range(self.arite,-1,-1):
            reg.append("([cde]\d*|[xyz]\d*|[fgh]\d*\(((?R))" +",((?R))"*i + "\))")
        result = regex.findall(r"%s" %('|').join(reg), self.value)
        out = []
        for n_uplet in result:
            for elem in n_uplet:
                if elem != '':
                    out.append(elem)
        self.args = out[1:]
        self.arite = len(self.args)
    def get_type(self):
        const = "^[cde]\d*$"
        var = "^[xyz]\d*$"
        fonc = "^[fgh]\d*\(.*\)$"
        if regex.match(r"%s" %const, self.value):
            return (self.value, 'constante')
        elif regex.match(r"%s" %var, self.value):
            return (self.value, 'variable')
        elif regex.match(r"%s" %fonc, self.value):
            return (regex.findall(r"^([fgh]\d*)\(.*\)$",
self.value)[0], 'fonction')
        return
    def show(self, tab = ''):
        if self.type == 'fonction':
            if tab == '':
                out = tab + '- ' + '<%s(%d)> %s(%s) :' %(self.type, self.arite, self.name, (',').join(self.args))
            else:
                out = '\n' + tab + '- ' + '<%s(%d)> %s(%s) :' %(self.type, self.arite, self.name, (',').join(self.args))
            out += tab + self.show_args(tab + '    ')
        else:
            out = '\n' + tab + '- <%s> %s' %(self.type, self.name)
        return out
    def show_args(self, tab=''):
        out = tab
        for elem in self.args:
            current = term(elem)
            out += current.show(tab)
        return out
    def interpreter(self, inter):
        if self.type == 'fonction':
            return getattr(inter, self.name)(self.interpreter_args(inter))
        else:
            return getattr(inter, self.name)
    def interpreter_args(self, inter):
        out = []
        for elem in self.args:
            element = term(elem)
            if element.type == 'fonction':
                out.append(getattr(inter, element.name)(element.interpreter_args(inter)))
            else:
                out.append(getattr(inter, element.name))
        return tuple(out)
inter1 = interpretation(str_f, str_g, str_h, str_c1, str_c2, str_c3)
inter2 = interpretation(int_f, int_g, int_h, int_c1, int_c2, int_c3)
t = term("f(c1,c2,h(g(h(c1,c2)),c3),g(c1))")
print(t.show())
print("Le terme 't' est interprete dans inter1 par [t]^inter1 = ",
t.interpreter(inter1))
print("Le terme 't' est interprete dans inter2 par [t]^inter2 = ",
t.interpreter(inter2))
