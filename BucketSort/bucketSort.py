#BucketSort

import time
import random
import matplotlib.pyplot as plt
tempos=[]

tamanho =  [15000,25000,35000,45000,550000]

def geraVetor(tamanho):
    vetor = list(range(tamanho,0,-1))
    random.shuffle(vetor)
    return vetor

def bucketsort(vetor):
    antes = time.time()
    tamanhoVetor = len(vetor)
    balde = [[] for _ in range(tamanhoVetor)]
    maior = max(vetor)
    tamanho = maior/tamanhoVetor

    for i in range(tamanhoVetor):
        j = int(vetor[i] / tamanho)
        if j != tamanhoVetor:
            balde[j].append(vetor[i])
        else:
            balde[tamanhoVetor - 1].append(vetor[i])

    for i in range(tamanhoVetor):
        insertionsort(balde[i])

    vetor_ok = []
    for i in range(tamanhoVetor):
        vetor_ok = vetor_ok + balde[i]
    depois = time.time()
    return (depois-antes)


def insertionsort(vetor):
    for i in range(1, len(vetor)):
        atual = vetor[i]
        j = i - 1
        while j >= 0 and atual < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = atual


for i in range(len(tamanho)):
  tempo=bucketsort(geraVetor(tamanho[i]))
  tempos.append(tempo)
  print(vetor)

plt.plot(tamanho,tempos)
plt.show()
