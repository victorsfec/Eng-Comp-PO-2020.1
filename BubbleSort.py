import time
from random import randint
import matplotlib.pyplot as plt
tempos=[]
def geraVetor(tam):
    vetor = []
    while len(vetor) < tam:
        n = randint(1,tam)
        if n not in vetor: vetor.append(n)
    return vetor

def bubbleSort(arr):
    antes=time.time()
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            count+=1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    depois=time.time()
    return count,(depois-antes)
  
vetor = [1000,10000,30000,60000]

for i in range(len(vetor)):
  saida,tempo=bubbleSort(geraVetor(vetor[i]))
  saidaB.append(saida)
  tempos.append(tempo)

plt.plot(vetor,tempos)
plt.show()
