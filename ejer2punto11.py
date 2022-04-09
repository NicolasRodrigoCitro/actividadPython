nombres1 =open("nombres_1.txt",encoding='utf8')
nombres2 = open("nombres_2.txt",encoding='utf8')
eval1 = open("eval1.txt")
eval2= open("eval2.txt")

lista_nombres1=[nombre.replace(',','').replace('\n','').replace("'","").strip() for nombre in nombres1.readlines()]
lista_nombres2=[nombre.replace(',','').replace('\n','').replace("'","").strip() for nombre in nombres2.readlines()]
lista_eval1=[nota.replace(',','').replace('\n','').replace("'","").strip() for nota in eval1.readlines()]
lista_eval2=[nota.replace(',','').replace('\n','').replace("'","").strip() for nota in eval2.readlines()]

nombres1.close()
nombres2.close()
eval1.close()
eval2.close()
'''nombres_coincidentes=(set(lista_nombres2) & set(lista_nombres1))
nombres_coincidentes = list(nombres_coincidentes)
nombres_coincidentes.sort()
print(nombres_coincidentes)'''
def suma_de_numeros(unNumero1,unNumero2):
    return int(unNumero1+unNumero2)
listaEval2 = list(map(int,lista_eval1))
listaEval2 = list(map(int,lista_eval2))
i=0
for n in lista_nombres1:
    print(f"Nombre: {lista_nombres1[i]} eval1: {lista_eval1[i]} eval2: {lista_eval2[i]} suma { (int(lambda x: lista_eval1[i]+lista_eval2[i])) }")
    i+=1