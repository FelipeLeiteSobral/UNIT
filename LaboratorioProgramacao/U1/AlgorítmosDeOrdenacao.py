# Bubble Sort (Bubble sort é o algoritmo mais simples, mas o menos eficientes. Neste algoritmo cada elemento 
# da posição i será comparado com o elemento da posição i + 1, ou seja, um elemento da posição 2 será 
# comparado com o elemento da posição 3. Caso o elemento da posição 2 for maior que o da posição 3, 
# eles trocam de lugar e assim sucessivamente)

listaDeNumerosDesordenados = [9,2,3,8,12,93,45,33,29,55]

def bubbleSort(): 
    for i in range(listaDeNumerosDesordenados):
        for j in range(listaDeNumerosDesordenados):
            if 