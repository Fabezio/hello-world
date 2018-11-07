# coding:utf-8
''' 
ce script sert à calculer selon l'algorithme de Gauss, avec uniquement des entiers positifs pairs.

la fonction est la suivante: f(x)=(x/2)²+x/2 - C'est celle-ci que je vais mettre en application
'''
x = int(input ("entrez le nombre pair à calculer: "))
if (x%2)==0:
	print (x)

	z = x/2
	y = str(z**2+z)
	print ("le résultat est:",y)
else: 
	print("nombre impair, recommencez!")
