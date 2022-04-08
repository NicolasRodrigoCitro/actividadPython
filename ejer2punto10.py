nombres =open("nombres_1.txt", encoding='utf8')
evaluacion1 = open("eval1.txt")
evaluacion2 = open("eval2.txt")

lista=[x.replace(',','').replace('\n','').replace("'","").strip() for x in nombres.readlines()]

unEval1 = [x.replace(',','').replace('\n','').replace("'","").strip() for x in evaluacion1.readlines()]
listaEval1 = list(map(int,unEval1))

unEval2 =[x.replace(',','').replace('\n','').replace("'","").strip() for x in evaluacion2.readlines()]
listaEval2 = list(map(int,unEval2))

def suma_de_numeros(unNumero1,unNumero2):
    return int(unNumero1+unNumero2)
alumnos={}
i=0
for u in lista:
 clave=lista[i]
 alumnos[clave]=suma_de_numeros(listaEval1[i],listaEval2[i])
 i+=1
#print(alumnos)


total=0
cantidad=0
for valor in alumnos.values():
 total= total + valor
 cantidad+=1
promedio=total/cantidad

for clave, valor in alumnos.items():
 if(valor<promedio):
  print(f"el alumno {clave} no supero el promedio de {promedio} su nota es: {valor}")