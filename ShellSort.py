#SHELLSORT
import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    random.shuffle(vetor)
    return vetor

def shell_sort(vetor):
    antes=time.time()
    tamanho = len(vetor)
    intervalo = tamanho // 2

    while intervalo > 0:
        for i in range(intervalo, tamanho):
            aux = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > aux:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = aux
        intervalo //= 2
    depois=time.time()
    return (depois-antes)
  
tam = [30000,40000,50000,60000,70000]

for i in range(len(vetor)):
  tempo=shell_sort(geraVetor(vetor[i]))
  tempos.append(tempo)

plt.plot(vetor,tempos)
plt.show()
