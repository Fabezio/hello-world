# coding:utf-8
''' 
ce script sert à calculer selon l'algorithme de Gauss, avec uniquement des entiers positifs impairs.

la fonction est la suivante: f(x)=[(x+1)/2]² - C'est celle-ci que je vais mettre en application
'''
x = int(input ("entrez le nombre impair à calculer: "))
if (x%2)!=0:
	print (x)
	y = str(((x+1)/2)**2)
	print ("le résultat est:",y)
else: 
	print("nombre pair, recommencez!")
