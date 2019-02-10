# Homework 4 CS: 3330
# Includes HeapSort

import math
import random

L1 = random.sample(range(100), 50)
L2 = random.sample(range(1000), 100)
L3 = random.sample(range(10000), 1000)
L4 = random.sample(range(100000), 10000)


def selectionsort(arr):
    comparisons = 0
    length = len(arr)
    for i in range(length):
        minimum = i
        for j in range(i+1, length):
            comparisons += 1
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return comparisons


L1I = L1[:]
L2I = L2[:]
L3I = L3[:]
L4I = L4[:]

L1Q = L1I[:]
L2Q = L2I[:]
L3Q = L3I[:]
L4Q = L4I[:]

L1M = L1Q[:]
L2M = L2Q[:]
L3M = L3Q[:]
L4M = L4Q[:]

L1H = L1Q[:]
L2H = L2Q[:]
L3H = L3Q[:]
L4H = L4Q[:]

print("Selection sort running times in terms of comparisons made: ")
print("N = 50: " + str(selectionsort(L1)))
print("N = 100: " + str(selectionsort(L2)))
print("N = 1000: " + str(selectionsort(L3)))
print("N = 10000: " + str(selectionsort(L4)))




def insertionsort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1

        # Since we make 2 comparisons in the while loop, we increment comparisons by 2

        while j >= 0 and arr[j] > v:
            comparisons += 2
            arr[j + 1] = arr[j]
            j -= 1

        comparisons += 1
        arr[j + 1] = v

    return comparisons


print("")
print("Insertion sort running times in terms of comparisons made: ")

print("N = 50: " + str(insertionsort(L1I)))
print("N = 100: " + str(insertionsort(L2I)))
print("N = 1000: " + str(insertionsort(L3I)))
print("N = 10000: " + str(insertionsort(L4I)))


def partition(arr, l, r):
    global comparisonforQuick
    s = l  # index of smaller element
    pivot = arr[l]  # pivot

    for j in range(l + 1, r+1):
        comparisonforQuick += 1
        if arr[j] < pivot:
            s = s + 1
            arr[s], arr[j] = arr[j], arr[s]

    arr[s], arr[l] = arr[l], arr[s]
    return s


def quicksort(arr, l, r):
    global comparisonforQuick
    comparisonforQuick += 1
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s - 1)
        quicksort(arr, s+1, r)
    return comparisonforQuick



print("")
print("Quicksort running times in terms of comparisons made: ")

comparisonforQuick = 0
print("N = 50: " + str(quicksort(L1Q, 0, len(L1Q) - 1)))

comparisonforQuick = 0
print("N = 100: " + str(quicksort(L2Q, 0, len(L2Q) - 1)))

comparisonforQuick = 0
print("N = 1000: " + str(quicksort(L3Q, 0, len(L3Q) - 1)))

comparisonforQuick = 0
print("N = 10000: " + str(quicksort(L4Q, 0, len(L4Q) - 1)))

def mergeSort(alist):
    global comparisonforMerge

    comparisonforMerge += 1
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            comparisonforMerge += 1
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            comparisonforMerge += 1
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        comparisonforMerge += 1

        while j < len(righthalf):
            comparisonforMerge += 1
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
        comparisonforMerge += 1
    return comparisonforMerge

print("")
print("Mergesort running times in terms of comparisons made: ")

comparisonforMerge = 0
print("N = 50: " + str(mergeSort(L1M)))

comparisonforMerge = 0
print("N = 100: " + str(mergeSort(L2M)))

comparisonforMerge = 0
print("N = 1000: " + str(mergeSort(L3M)))

comparisonforMerge = 0
print("N = 10000: " + str(mergeSort(L4M)))



def heapify(arr, n, i):
    global comparisonforHeap
    largest = i
    l = 2*i+1
    r = 2*i+2
    comparisonforHeap+=2
    if l < n and arr[i] < arr[l]:
        largest = l

    comparisonforHeap += 1 # On average
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        heapify(arr, n, largest)


def heapsort(arr):
    global comparisonforHeap
    n = len(arr)
	
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
		
    return comparisonforHeap



print("")
print("Heapsort running times in terms of comparisons made: ")

comparisonforHeap = 0
print("N = 50: " + str(heapsort(L1H)))

comparisonforHeap = 0
print("N = 100: " + str(heapsort(L2H)))

comparisonforHeap = 0
print("N = 1000: " + str(heapsort(L3H)))

comparisonforHeap = 0
print("N = 10000: " + str(heapsort(L4H)))
