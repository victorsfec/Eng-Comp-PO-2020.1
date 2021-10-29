#RADIXSORT

import time
import random
import matplotlib.pyplot as plt
tempos=[]

tamanho = [20000,30000,40000,50000,60000]

def geraVetor(tamanho):
    vetor = list(range(tamanho,0,-1))
    random.shuffle(vetor)
    return vetor

def radixSort(vetor):
    antes=time.time()
    base = 1
    maior = max(vetor)

    while maior/base > 0:
        indice = len(vetor) + 1
        count = [0] * indice

        for i in vetor:
            count[i] += 1

        k = 0

        for i in range(indice):
            for j in range(count[i]):
                vetor[k] = i
                k += 1
        base *= 10
        depois=time.time()
        return(depois-antes)

for i in range(len(tamanho)):
  tempo=radixSort(geraVetor(tamanho[i]))
  tempos.append(tempo)

plt.plot(tamanho,tempos)
plt.show()
