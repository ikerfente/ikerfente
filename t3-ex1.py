'''Fes un programa que suma un valor introduït per teclat a tots els elements
de la llista [1,2,3,4,5,6,7,8,9,10] utilitzant un bucle for. Cal modificar
la llista original.
'''

llista=[1,2,3,4,5,6,7,8,9,10]
num = int(input("Introdueix un nombre: "))
for i in range(len(llista)):
    llista[i]=llista[i]+num
    print(llista[i], end=" ")