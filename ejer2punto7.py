cadena = input("ingrese una palabra o una frase ")
hetereograma = True
i=0
conjunto_letras=[]
while(hetereograma == True and i < len(cadena)):
    letra=cadena[i]
    if letra in conjunto_letras:
        hetereograma=False
        print("no es un hetereograma")
    else:
        conjunto_letras.append(letra)
    i += 1
if(hetereograma == True):
    print("es un hetereograma")

