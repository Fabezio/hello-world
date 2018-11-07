# coding:utf-8
''' 
ce programme sert à calculer selon l'algorithme de Gauss, la fameuse méthode d'addition de nombres se suivant à partir de 1.
le principe est simple: soit une suite de nombre entiers de 1 à x, qu'il faut additionner; 
la fonction est la suivante: f(x)=(x²+x)/2 - C'est celle-ci que je vais mettre en application
'''
x = int(input ("entrez le nombre à calculer: "))
print (x)
y = str((x**2+x)/2)
print ("le résultat est:",y)