import sqlite3
import webbrowser
import os

repertoire_courant = 'VOTRE REPERTOIRE DE TRAVAIL ICI'

class journal:
    def __init__(self):
        os.chdir(repertoire_courant)
        con = sqlite3.connect("articles.db")
        cur = con.cursor()
        res = cur.execute("SELECT name FROM sqlite_master WHERE name='articles'")
        if res.fetchone() is None:
            cur.execute("""
            CREATE TABLE articles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre VARCHAR(100) NOT NULL,
                auteur VARCHAR(100) NOT NULL,
                contenu VARCHAR(5000) NOT NULL,
                CONSTRAINT unicite UNIQUE (titre, auteur, contenu)
            );""")
        self.con = con
        self.cur = cur
        self.articles = []
    def maj(self):
        res = self.cur.execute("select * FROM articles")
        self.articles = []
        for elem in res.fetchall():
            item = article(elem[1], elem[2], elem[3])
            self.articles.append(item)
    def ajoute(self, titre, auteur, contenu):
        art = article(titre, auteur, contenu)
        art.rec(self.con, self.cur)
        self.maj()
    def close(self):
            self.con.close()
    def html(self):
        html_template = "<!doctype html>\n"
        html_template += "<html lang='fr'>\n"
        html_template += "<head>\n"
        html_template += "\t<meta charset='utf-8'>\n"
        html_template += "\t<title>Le journal de l'&eacute;cole</title>\n"
        html_template += "\t<link href='journal.css' rel='stylesheet'>"
        html_template += "</head>\n"
        html_template += "<body>\n"
        html_template += "\t<div class='journal'>\n"
        html_template += "\t<div class='header'>Le journal de l'&eacute;cole</div>\n"
        for elem in self.articles:
            html_template += elem.html()
        html_template += "\t</div>\n"
        html_template += "</body>\n"
        f = open('index.html', 'w')
        f.write(html_template)
        f.close()
        webbrowser.open('index.html')

class article:
    def __init__(self, titre, auteur, contenu):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
    def tab(self):
        return (self.titre, self.auteur, self.contenu)
    def rec(self, con, cur):
        res = cur.execute("SELECT titre FROM articles WHERE titre=? AND auteur=? AND contenu=?", self.tab())
        if res.fetchone() is None:
            cur.execute("INSERT INTO articles (titre, auteur, contenu) VALUES (?,?,?)", self.tab())
            con.commit()
    def html(self):
        html_template = "\t\t<div class='article'>\n"
        html_template += f"\t\t\t<div class='titre'>{self.titre}</div>\n"
        html_template += f"\t\t\t<p class='contenu'>{self.contenu}</p>\n"
        html_template += f"\t\t\t<div class='auteur'>{self.auteur}</div>\n"
        html_template += "\t\t</div>\n"
        return html_template

news = journal()
news.ajoute("Et superbas superbas parens leges.", "R.T","Impetrare vidimus hoc aut aut habeat accepimus de velint amicis amicis sunt ante si eorum iis ante nobis velimus Ex concedere quos res vitii memoriam res communis aut statuerimus exempla de et numero et simus quidquid qui ante velimus quibus iis vitii si ad vidimus vidimus accedunt amicis si res velint et iis impetrare accedunt vel rectum loquimur quibus ab Ex amicis sunt sapientiam nihil qui sunt numero eorum quidem vita sed qui de ante iis ab et maxime hoc amicis Ex de eorum nobis proxime memoriam rectum communis res quidquid memoriam vel velint simus novit quidquid sapientia Ex sed.")
news.ajoute("Ubi posse nec quos praefuit.", "A.B","In ac admiratione nullo meis virtutis quadam sunt sapientia ut utilitates quisque auxit omnia ego sic confidit ac quisque multae excellit se consecutae magnae est maxime posita quidem quisque vicissim non Minime nullo maxime earum ut non enim in virtute maxime ego consecutae ut ac spe posita amicitiis sic hercule indigens nulla sapientia et ab virtutis et expetendis Sed expetendis quadam nullo ita ab nullo benevolentiam se admiratione in egeat maxime ego quadam ille illius dilexit quadam quisque ita meis quamquam profectae virtutis utilitates tamen et hercule sed in quisque excellit Africanus iudicet fortasse vicissim Sed magnae Quid Africanus egeat.")
news.ajoute("Securitas concitat concitat cum rati.", "E.S","Ante omnibus publicae profecto Ille omnibus anteferre laus maxime M ipso et cum cum laus beneficio paulo dignitatemque paulo me paulo in in quo omnis beneficio concessisti enim sit est M accepto concessisti anteferre ordinis sit sed ante publicae die ante die praesertim maximo summo profecto intellegis suspicionibus tum Ex actae te cum rei doloribus in paulo M sit sit doloribus dato cum in te maximo praesertim maxime M sit doloribus vel quidem et publicae tuo rei profecto commemoratis quo tanta vitae huius multis dignitatemque actae multis die quidem Ille vel omnibus iudicio te dignitatemque beneficio intellegis doloribus dignitatemque gravissimo.")
news.ajoute("Nisi faciunt quodam se se.", "U.V","Ut iustissimus et miserabiles est tribunis exitio ad pluribus in ausus non cognomentum vinctum iam Paulum artifex defensantem languente ausus excessit genere exitio ad vinctum in rector miserabiles inpegit percitus percitus inditum vicarium hocque languente communium eum defensantem iustissimus tribunis ad multorum deformi genere urgente genere adoritur pluribus cum non deformi deformi urgente ausus rector e imperatoris Paulus imperatoris iustissimus vita hocque quia excessit cum inditum urgente periculorum eum hoc suum ut praeerat vinctum levare in aliis cum conplicandis imperatoris quibus comitatum levare perduceret: ut unde adhuc inditum est comitatum Paulum excessit ut aliis rector eum adhuc artifex ad excessit.")
news.html()
news.close()
