'''Escriviu un programa per obtenir el nombre més gran, més petit i la mitjana d'una llista de 
1000 sencers generada aleatòriament (del -5000 al 5000).
Feu 2 versions: versió bucle i versió mètodes.
'''
import random
from statistics import mean

llista=[]
N=1000

#nll=int(input("Introdueix la quantitat d'elements de la llista: "))

#Versió bucle
for i in range(N):
    val=random.randint(-5000, 5000)
    llista.append(val)

    #Anem calculant mínim, màxim i suma
    if i==0:
        minim=maxim=sum=llista[0]
    else:        
        if llista[i]<minim:
            minim=llista[i]
            
        if llista[i]>maxim:
            maxim=llista[i]
        #Anem acumulant els valors per fer la mitjana
        sum+=llista[i]
        
mitj=sum/N

print("\nResultats de la versió feta amb bucles:")
print("\nLa mitjana és", mitj)
print("Mínim:", minim)
print("Màxim:", maxim)

print("\nResultats de la versió feta amb mètodes:")
print("\nLa mitjana és", mean(llista))
print("Mínim:", min(llista))
print("Màxim:", max(llista))