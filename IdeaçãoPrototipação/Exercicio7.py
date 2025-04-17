arrayList = [4,5,1,2,10,0]

#Algorítimo de ordenação Bubble sort

def BublleSort(array):
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return print(array)

BublleSort(arrayList)


# Algorítimo de ordenação Insertion Sort

def InsertionSort(array):
    for i in range (len(array)):
        elementoCorrente = array[i]
        j = i+1
        while j < len(array) and array[j] > elementoCorrente:
            array[j-1] = array[j]
            j += 1
            