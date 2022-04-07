'''3. Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string'''
readme="hola mundo mi mundo"
letra = input("Ingrese una letra: ")

texto = readme.lower().split()
print(texto)
for n in texto:
    if(n.startswith(letra)):
        print(n)
    else:
        print("Ver: módulo string")


