import lambdaCalcul
from lambdaCalcul import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import *
import re

class bouton():
    '''Classe des boutons de la calculatrice'''
    def __init__(self, valeur):
        self.value = valeur

class paveNumerique():
    '''Classe de l'ensemble des boutons numeriques de la calculatrice'''
    def __init__(self):
        self.value = []
    def ajoute(self, button):
        self.value.append(button)

class paveOperations():
    '''Classe de l'ensemble des boutons d'operation de la calculatrice'''
    def __init__(self):
        self.value = []
    def ajoute(self, button):
        self.value.append(button)

class fenetre(tk.Tk):
    '''Classe de la fenetre de la calculatrice'''
    def __init__(self, pavNumerique, pavOperations):
        self.width = 300
        self.height = 250
        self.monPaveNumerique = paveNumerique()
        self.monPaveNumerique = pavNumerique
        self.monPaveOperation = paveOperations()
        self.monPaveOperation = pavOperations
        tk.Tk.__init__(self)
        self.creer_widgets()
    def ecrireNumerique(self, valeur):
        self.entry.insert(END, valeur)
    def ecrireOperation(self, valeur):
        self.entry.insert(END, self.monPaveOperation.value[valeur].value)
    def effacer(self):
        self.entry.delete(0, 'end')
    def traiteOperateur(self, nbs, ops, operateur, nbOps, out):
        '''Filtre de calcul sur un operateur'''
        i = 0
        while ops.count(operateur) > 0:
            if ops[i] == operateur:
                if nbOps == 0:
                    out = self.resultOperation(entiers(int(nbs[i])), ops[i], entiers(int(nbs[i + 1])))
                    nbOps +=1
                    nbs.pop(i)
                    nbs.pop(i)
                    ops.pop(i)
                else:
                    out = self.resultOperation(out, ops[i], entiers(int(nbs[i])))
                    nbs.pop(i)
                    ops.pop(i)
            else:
                if i < len(ops) - 1:
                    i += 1
        return (out, nbs, ops, nbOps)
    def operation(self, nbs, ops):
        '''Traitement des operations en respectant  PEMDAS'''
        nbOps = 0
        out = entiers(0)
        out, mynbs, myops, nbOps = self.traiteOperateur( nbs, ops, '^', nbOps, out)
        out, mynbs, myops, nbOps = self.traiteOperateur( mynbs, myops, '*', nbOps, out)
        out, mynbs, myops, nbOps = self.traiteOperateur( mynbs, myops, '/', nbOps, out)
        out, mynbs, myops, nbOps = self.traiteOperateur( mynbs, myops, '+', nbOps, out)
        out, mynbs, myops, nbOps = self.traiteOperateur( mynbs, myops, '-', nbOps, out)
        return out
    def resultOperation(self, nb1, op, nb2):
        '''Retourne le resultat d'une operation sous forme d'entiers'''
        if op == '-':
            return nb1 - nb2
        elif op == '*': 
            return nb1 * nb2
        elif op == '+': 
            return nb1 + nb2
        elif op == '^': 
            return nb1 ** nb2
        elif op == '/': 
            return nb1 // nb2
        elif op == '%': 
            return nb1 % nb2
    def comparateur(self, nb1, op, nb2):
        '''Retourne le resultat d'un comparateur sous forme de booleen'''
        if op == '<':
            return nb1 < nb2
        elif op == '<=': 
            return nb1 <= nb2
        elif op == '>': 
            return nb1 > nb2
        elif op == '>=': 
            return nb1 >= nb2
        elif op == '=': 
            return nb1 == nb2
        elif op == '!=': 
            return nb1 != nb2
    def verifier(self):
        '''Detection des patterns de la saisie pour un traitement distingue'''
        operation = "( )*[0-9]+( )*([-*+^/%])+( )*[0-9]+( )*(([-*+^/%])+( )*[0-9]+)*"
        comparateur = "( )*((<|>)|(<|>)=|=|!=)( )*"
        nombre = "( )*[0-9]+( )*"
        pattern = []
        pattern.append("^" + nombre + "$")
        pattern.append("^" + operation + "$")
        pattern.append("^" + nombre + comparateur + nombre + "$")
        pattern.append("^" + nombre + comparateur + operation + "$")
        pattern.append("^" + operation + comparateur + nombre + "$")
        pattern.append("^" + operation + comparateur + operation + "$")#
        mypattern = '|'.join(pattern)
        if re.search(mypattern, self.entry.get()) :
            if re.search("^" + nombre + "$", self.entry.get()):
                out = entiers(int(self.entry.get()))
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())
            elif re.search("^" + operation + "$", self.entry.get()):
                resultNb = re.findall("\d+", self.entry.get())
                resultOp = re.findall("[-*+^/%]+", self.entry.get())
                out = self.operation(resultNb, resultOp)
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())
            elif re.search("^" + nombre + comparateur + nombre + "$", self.entry.get()):
                #traitement nombres
                resultNb = re.findall("\d+", self.entry.get())
                nb1 = entiers(int(resultNb[0]))
                nb2 = entiers(int(resultNb[1]))
                #traitement comparateur
                resultOp = re.findall("[<>=!]+", self.entry.get())
                out = self.comparateur(nb1, resultOp[0], nb2)
                #affichage
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())
            elif re.search("^" + nombre + comparateur + operation + "$", self.entry.get()):
                #traitement nombre
                resultNb = re.findall("^(\d+)", self.entry.get())
                nb1 = entiers(int(resultNb[0]))
                #traitement operation
                operation = re.findall("^\d+[<>=!]+([0-9-*+^/%]*)$", self.entry.get())
                resultNb = re.findall("\d+", operation[0])
                resultOp = re.findall("[-*+^/%]+", operation[0])
                nb2 = self.operation(resultNb, resultOp)
                #traitement comparateur
                resultcomp = re.findall("[<>=!]+", self.entry.get())
                out = self.comparateur(nb1, resultcomp[0], nb2)
                #affichage
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())
            elif re.search("^" + operation + comparateur + nombre + "$", self.entry.get()):
                #traitement operation
                operation = x = re.findall("^([0-9-*+^/%]*)[<>=!]+\d+$", self.entry.get())
                resultNb = re.findall("\d+", operation[0])
                resultOp = re.findall("[-*+^/%]+", operation[0])
                nb1 = self.operation(resultNb, resultOp)
                #traitement nombre
                nombre = re.findall("^[0-9-*+^/%]*[<>=!]+(\d+)$", self.entry.get())
                nb2 = entiers(int(nombre[0]))
                #traitement comparateur
                resultcomp = re.findall("[<>=!]+", self.entry.get())
                out = self.comparateur(nb1, resultcomp[0], nb2)
                #affichage
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())
            elif re.search("^" + operation + comparateur + operation + "$", self.entry.get()):
                #traitement operation 1
                operation = x = re.findall("^([0-9-*+^/%]*)[<>=!]+[0-9-*+^/%]*$", self.entry.get())
                resultNb = re.findall("\d+", operation[0])
                resultOp = re.findall("[-*+^/%]+", operation[0])
                nb1 = self.operation(resultNb, resultOp)
                #traitement operation 2
                operation = x = re.findall("^[0-9-*+^/%]*[<>=!]+([0-9-*+^/%]*)$", self.entry.get())
                resultNb = re.findall("\d+", operation[0])
                resultOp = re.findall("[-*+^/%]+", operation[0])
                nb2 = self.operation(resultNb, resultOp)
                #traitement comparateur
                resultcomp = re.findall("[<>=!]+", self.entry.get())
                out = self.comparateur(nb1, resultcomp[0], nb2)
                #affichage
                self.entry.delete(0, 'end')
                self.entry.insert(END, out.show())               
        else:
            self.entry.delete(0, 'end')
            self.entry.insert(END, 'Erreur')
    def creer_widgets(self):
        '''Creation de la fenetre'''
        self.size = str(self.width) + "x" + str(self.height)
        self.entry = tk.Entry (self, 
                               font=("Calibri",14),
                               justify="right",
                               width=6,bg="#1E6FBA",
                               fg="yellow",
                               disabledbackground="#1E6FBA",
                               disabledforeground="yellow",
                               highlightbackground="black",
                               highlightcolor="red",
                               highlightthickness=1,
                               bd=0)
        self.entry.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        ipadx=10,
                        columnspan=6,
                        sticky=EW)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=3)
        self.columnconfigure(5, weight=3)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.frm = Frame(self, padx=10, pady=10)
        btn = []
        exe = Button(self,
                     text = 'EXE',
                     fg = 'red',
                     command=self.verifier)
        exe.grid(row = 1,
                 column = 5,
                 pady=5,
                 padx=2,
                 ipady=2,
                 sticky=EW)
        c = Button(self,
                   text = 'C',
                   fg = 'red',
                   command=self.effacer)
        c.grid(row = 1,
               column = 4,
               pady=5,
               padx=2,ipady=2,sticky=EW)
        for index, but in enumerate(self.monPaveNumerique.value):
            btn.insert(index, Button(self,
                                     text = but.value,
                                     fg = 'blue',
                                     command=partial(self.ecrireNumerique, index)))
            btn[index].grid(row = ( index // 3) + 2,
                            column = index % 3,
                            padx=2,
                            pady=2,
                            sticky=EW)
        for index, but in enumerate(self.monPaveOperation.value):
            btn.insert(index, Button(self, text = but.value,
                                     fg = 'blue',
                                     command=partial(self.ecrireOperation, index)))
            btn[index].grid(row = ( index // 2) + 2,
                            column = (index % 2)+4,
                            pady=2,
                            padx=2,
                            sticky=EW)  
        self.geometry(self.size)

if __name__ == "__main__":
    button0 = bouton('0')
    button1 = bouton('1')
    button2 = bouton('2')
    button3 = bouton('3')
    button4 = bouton('4')
    button5 = bouton('5')
    button6 = bouton('6')
    button7 = bouton('7')
    button8 = bouton('8')
    button9 = bouton('9')
    button10 = bouton('+')
    button11 = bouton('-')
    button12 = bouton('*')
    button13 = bouton('^')
    button14 = bouton('/')
    button15 = bouton('%')
    button16 = bouton('<')
    button17 = bouton('>')
    button18 = bouton('=')
    touchesNumeriques = paveNumerique()
    touchesNumeriques.ajoute(button0)
    touchesNumeriques.ajoute(button1)
    touchesNumeriques.ajoute(button2)
    touchesNumeriques.ajoute(button3)
    touchesNumeriques.ajoute(button4)
    touchesNumeriques.ajoute(button5)
    touchesNumeriques.ajoute(button6)
    touchesNumeriques.ajoute(button7)
    touchesNumeriques.ajoute(button8)
    touchesNumeriques.ajoute(button9)
    touchesOperations = paveNumerique()
    touchesOperations.ajoute(button10)
    touchesOperations.ajoute(button11)
    touchesOperations.ajoute(button12)
    touchesOperations.ajoute(button13)
    touchesOperations.ajoute(button14)
    touchesOperations.ajoute(button15)
    touchesOperations.ajoute(button16)
    touchesOperations.ajoute(button17)
    touchesOperations.ajoute(button18)
    app = fenetre(touchesNumeriques, touchesOperations)
    app.title("Lambda Calculator")
    app.mainloop()