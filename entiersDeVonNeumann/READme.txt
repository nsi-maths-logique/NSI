Pour utiliser le module entiersDeVonNeumann :

Si le fichier entiersDeVonNeumann.py n'est pas dans le répertoire courant de votre programme. vous devez
ajouter ce fichier aux Path de Python. Pour cela, vous devez :

	- Avec Mac OS X et Linux, il faut taper la commande suivante depuis un shell Bash pour modifier
	la variable d'environnement PYTHONPATH :

		export PYTHONPATH=$PYTHONPATH:/chemin/vers/mon/super/module

	- Avec Windows, mais depuis un shell PowerShell, il faut taper la commande suivante :

		$env:PYTHONPATH += ";C:\chemin\vers\mon\super\module"

Vous pouvez alors utiliser la classe avec les commandes :

>>> import entiersDeVonNeumann
>>> from entiersDeVonNeumann import entiersDeVonNeumann

Et utiliser la classe entiersDeVonNeumann librement :

>>> n10 = entiersDeVonNeumann(10)
>>> n10.show()
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}