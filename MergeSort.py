#MERGESORT
import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    #random.shuffle(vetor)
    return vetor

def merge_sort(vetor):
    if len(vetor) > 1:
        meio = len(vetor)//2
        esquerda = vetor[:meio]
        direita = vetor[meio:]
        mergesort(esquerda)
        mergesort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    
vetor = [20000,40000,60000,80000,100000]

for i in range(len(vetor)):
  antes=time.time()
  tempo=merge_sort(geraVetor(vetor[i]))
  depois=time.time()
  tempo=depois-antes
  tempos.append(tempo)

plt.plot(vetor,tempos)
plt.show()
