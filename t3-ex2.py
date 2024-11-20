'''Escriviu un programa que mostri per pantalla el resultat de sumar i el resultat de multiplicar
tots els elements d'una llista. Cal introduir la llista per teclat.
Ajuda: feu servir un bucle per afegir elements a la llista, un cop afegits mostreu la llista
per pantalla i després utilitzeu un for per fer els càlculs.

pe ex la llista entrada per teclat és [10,20,30] el resultat de sumar és 60 i el resultat de
multiplicar és 6000.
'''
ll=[]
suma=0
mult=1

nll=int(input("Introdueix la quantitat d'elements de la llista: "))

for i in range(nll):
    ele=int(input("Introdueix l'element "+str(i+1)+" de la llista: "))
    ll.append(ele)

print ("La llista introduida es: ", ll)

for i in range(len(ll)):
    suma+=ll[i]
    mult*=ll[i]

print("El resultat de sumar els valors de la llista es: ", suma)
print("El resultat de multiplicar els valors de la llista es: ", mult)