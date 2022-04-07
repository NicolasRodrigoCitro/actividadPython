from math import factorial
from pickle import FALSE, TRUE


evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

texto=evaluar.splitlines()#me devuelve una lista con los datos donde hay un salto de linea
ok=FALSE
if(len(texto[0].split()) <= 10):
        ok=TRUE
unDiccionario={"facil":0,"aceptable":0,"dificil":0,"muy dificil":0}
for u in texto[1:]:
    if(len(u.split()) <= 12):
        unDiccionario["facil"]= unDiccionario["facil"] + 1
    elif (len(u.split())>=13 and len(u.split()) <= 17):
        unDiccionario["aceptable"]=unDiccionario["aceptable"] + 1
    elif (len(u.split())>=18 and len(u.split()) <= 25):
        unDiccionario["dificil"]=unDiccionario["dificil"] + 1
    else:
        unDiccionario["muy dificil"]=unDiccionario["muy dificil"] + 1
print(unDiccionario)
