lista_nombres=['Agustin','Alan','Andrés', 'Ariadna','Bautista', 'CAROLINA', 'CESAR', 'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel',
'Fabián', 'Facundo', 'Facundo', 'FEDERICO', 'FEDERICO', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Jonathan', 'Jorge', 'JOSE', 'JUAN', 'Juan', 'Juan',
 'Julian', 'Julieta', 'LAUTARO', 'Leonel', 'LUIS', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'NICOLÁS', 'Noelia', 'Pablo', 'Priscila', 'TOMAS',
 'Tomás', 'Ulises', 'Yanina']
eval1=[
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
]
eval2=[30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
]
def suma_de_numeros(unNumero1,unNumero2):
    return (unNumero1+unNumero2)
alumnos={}
i=0
for u in lista_nombres:
 clave=lista_nombres[i]
 alumnos[clave]=suma_de_numeros(eval1[i],eval2[i])
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