Pour utiliser le module entiersDeZermelo :

Si le fichier entiersDeZermelo.py n'est pas dans le répertoire courant de votre programme. vous devez
ajouter ce fichier aux Path de Python. Pour cela, vous devez :

	- Avec Mac OS X et Linux, il faut taper la commande suivante depuis un shell Bash pour modifier
	la variable d'environnement PYTHONPATH :

		export PYTHONPATH=$PYTHONPATH:/chemin/vers/mon/super/module

	- Avec Windows, mais depuis un shell PowerShell, il faut taper la commande suivante :

		$env:PYTHONPATH += ";C:\chemin\vers\mon\super\module"

Vous pouvez alors utiliser la classe avec les commandes :

>>> import eentiersDeZermelo
>>> from entiersDeZermelo import entiersDeZermelo

Et utiliser la classe entiersDeZermelo librement :

>>> n10 = entiersDeZermelo(10)
>>> n10.show()
10