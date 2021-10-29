import time
import random
import matplotlib.pyplot as plt
tempos=[]

def geraVetor(tam):
    vetor = list(range(tam,0,-1))
    #random.shuffle(vetor)
    return vetor

def selection_sort(vetor):
    antes=time.time()
    count = 0
    flag = False
    for i in range(len(vetor)):
        min = i
        for j in range(i + 1, len(vetor)):
            count += 1
            if vetor[min] > vetor[j]:
                min = j

        aux = vetor[i]
        vetor[i] = vetor[min]
        vetor[min] = aux
        depois=time.time()
    return (depois-antes)
  
vetor = [1000,10000,30000,60000]

for i in range(len(vetor)):
  tempo=selection_sort(geraVetor(vetor[i]))
  tempos.append(tempo)

plt.plot(vetor,tempos)
plt.show()
