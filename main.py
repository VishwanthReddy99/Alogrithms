

import tkinter as tk

import time
import timeit

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def insertionsort():
	name = name_var.get()

	arr = name.split(',')
	for i in range(0,len(arr)):
		arr[i]=int(arr[i])
	starttime = timeit.default_timer()


	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j = j - 1
			arr[j + 1] = key

	
	time = timeit.default_timer() - starttime
	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the insertion sort alogirthm is " + str(time))
	label.place(x=500, y=500)
	print(str(time))
	root.mainloop()


def selectionsort():
	name = name_var.get()
	A = name.split(',')
	for i in range(0, len(A)):
		A[i] = int(A[i])
	starttime = timeit.default_timer()
	for i in range(len(A)):
		min = i
		for j in range(i + 1, len(A)):
			if A[j] < A[min]:
				min = j
		if min != i:
			tmp = A[min]
			A[min] = A[i]
			A[i] = tmp

	time = timeit.default_timer() - starttime

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		A) + " and The time taken to excute the selection sort alogirthm is " + str(time))
	label.place(x=500, y=400)
	print(str(time))

	root.mainloop()
def selectionsortcompare(arr):
	A = arr
	for i in range(0, len(A)):
		A[i] = int(A[i])
	starttime = timeit.default_timer()
	for i in range(len(A)):
		min = i
		for j in range(i + 1, len(A)):
			if A[j] < A[min]:
				min = j
		if min != i:
			tmp = A[min]
			A[min] = A[i]
			A[i] = tmp

	time = timeit.default_timer() - starttime

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		A) + " and The time taken to excute the selection sort alogirthm is " + str(time))
	print("secc"+str(time))

	label.place(x=500, y=400)



def merge(F, S):
	temp = []
	while (F and S):
		if F[0] >= S[0]:
			temp.append(S[0])
			S.remove(S[0])
		else:
			temp.append(F[0])
			F.remove(F[0])
	temp = temp + F + S

	return (temp)


def mergesort():
	name = name_var.get()
	arr = name.split(',')
	for i in range(0,len(arr)):
		arr[i]=int(arr[i])

	start_time = timeit.default_timer()

	if len(arr) == 1:
		return arr
	arr = mergearray(arr)
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the merge sort alogirthm is " + str(time))
	print(str(time))

	label.place(x=500, y=450)
	root.mainloop()

def mergesortcompare(arr):



	for i in range(0,len(arr)):
		arr[i]=int(arr[i])

	start_time = timeit.default_timer()

	if len(arr) == 1:
		return arr
	arr = mergearray(arr)
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the merge sort alogirthm is " + str(time))
	print("merg"+str(time))

	label.place(x=500, y=450)

def mergearray(arr):
	if len(arr) == 1:
		return arr
	n = len(arr)

	F = arr[0:(n // 2)]
	S = arr[(n // 2)::]
	F = mergearray(F)
	S = mergearray(S)
	return merge(F, S)


def max_heapify(A, l, i):
	large = i
	left = 2 * i
	right = (2 * i) + 1
	while left <= l and A[left] > A[large]:
		large = left
	while right <= l and A[right] > A[large]:
		large = right
	if large != i:
		A[large], A[i] = A[i], A[large]
		max_heapify(A, l, large)


def heapsort():
	name = name_var.get()
	A = [0]

	for i in range(0, len(A)):
		A[i] = int(A[i])
	A.extend(list(name.split(',')))
	for i in range(0, len(A)):
		A[i] = int(A[i])

	l = len(A) - 1
	for i in range((l // 2), 0, -1):
		max_heapify(A, l, i)
	print(A)
	start_time = timeit.default_timer()
	for i in range(l, 0, -1):
		A[l], A[1] = A[1], A[l]
		l = l - 1
		max_heapify(A, l, 1)
		print(A)

	time = timeit.default_timer() - start_time
	A.remove(0)
	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
			A) + " and The time taken to excute the heap sort alogirthm is " + str(time))
	print(str(time))

	label.place(x=500, y=350)
	root.mainloop()

def heapsortcompare(arr):
	A = [0]

	for i in range(0, len(A)):
		A[i] = int(A[i])
	A.extend(list(arr))
	for i in range(0, len(A)):
		A[i] = int(A[i])

	l = len(A) - 1
	for i in range((l // 2), 0, -1):
		max_heapify(A, l, i)
	start_time = timeit.default_timer()
	for i in range(l, 0, -1):
		A[l], A[1] = A[1], A[l]
		l = l - 1
		max_heapify(A, l, 1)
	time = timeit.default_timer() - start_time
	A.remove(0)
	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
			A) + " and The time taken to excute the heap sort alogirthm is " + str(time))
	print("heap"+str(time))

	label.place(x=500, y=350)


def Bubblesort():
	name = name_var.get()
	arr = name.split(',')
	for i in range(0,len(arr)):
		arr[i]=int(arr[i])
	start_time = timeit.default_timer()
	n = len(arr) - 1
	while (n != 0):
		for i in range(n):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		n = n - 1
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the Bubble sort  alogirthm is " + str(time))
	print(str(time))

	label.place(x=500, y=600)
	root.mainloop()
def Bubblesortcompare(arr):

	for i in range(0,len(arr)):
		arr[i]=int(arr[i])
	start_time = timeit.default_timer()
	n = len(arr) - 1
	while (n != 0):
		for i in range(n):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		n = n - 1
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the Bubble sort  alogirthm is " + str(time))
	print("bubble"+str(time))

	label.place(x=500, y=600)


def quicksort_main():
	name = name_var.get()
	arr = name.split(',')
	for i in range(0,len(arr)):
		arr[i]=int(arr[i])
	high = len(arr) - 1
	start_time = timeit.default_timer()

	arr=quick_reg(arr,0, high)
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the quick sort alogirthm is " + str(time))

	label.place(x=500, y=700)
	root.mainloop()
def quicksort_maincompare(arr):

	high = len(arr) - 1
	start_time = timeit.default_timer()

	arr=quick_reg(arr,0, high)
	time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the quick sort alogirthm is " + str(time))
	print("quic"+str(time))

	label.place(x=500, y=700)


def quick_reg(A, low, high):  # first element as pivot
    if low < high:
        j = partition(A, low, high)
        quick_reg(A, low, j - 1)
        quick_reg(A, j + 1, high)
    return A


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i < (len(arr) - 1) and arr[i + 1] < pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if i < j:
            tmp = arr[i + 1]
            arr[i + 1] = arr[j]
            arr[j] = tmp
            j = j - 1
    arr[low], arr[j] = arr[j], arr[low]
    return j

def compare():
	name = name_var.get()
	arr = name.split(',')
	for i in range(0, len(arr)):
		arr[i] = int(arr[i])


	inserstionsort_compare(arr)

	selectionsortcompare(arr)
	mergesortcompare(arr)
	heapsortcompare(arr)
	Bubblesortcompare(arr)
	quicksort_maincompare(arr)
	quicksort_medcompare(arr)




def inserstionsort_compare(arr):

	for i in range(0, len(arr)):
		arr[i] = int(arr[i])
	starttime = timeit.default_timer()
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j = j - 1
			arr[j + 1] = key
	time = timeit.default_timer() - starttime
	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the insertion sort alogirthm is " + str(time))
	print("inse"+str(time))

	label.place(x=500, y=500)


import statistics


def partition_median(array, leftend, rightend):
	length = rightend - leftend
	if length % 2 == 0:
		middle = array[int(leftend + length / 2 - 1)]
	else:
		middle = array[int(leftend + length / 2)]

	pivot = statistics.median([array[leftend], array[rightend - 1], middle])

	pivotindex = array.index(pivot)  # only works if all values in array unique

	array[pivotindex] = array[leftend]
	array[leftend] = pivot

	i = leftend + 1
	for j in range(leftend + 1, rightend):
		if array[j] < pivot:
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
			i += 1

	leftendval = array[leftend]
	array[leftend] = array[i - 1]
	array[i - 1] = leftendval
	return i - 1


def quicksort_median(array, leftindex, rightindex,mediancomparison):
	if leftindex < rightindex:
		newpivotindex = partition_median(array, leftindex, rightindex)

		mediancomparison += (rightindex - leftindex - 1)
		quicksort_median(array, leftindex, newpivotindex,mediancomparison)


		quicksort_median(array, newpivotindex + 1, rightindex,mediancomparison)
	return array

def quicksort_med():
	name = name_var.get()
	arr = name.split(',')
	for i in range(0, len(arr)):
		arr[i] = int(arr[i])
	mediancomparison = 0
	start_time = timeit.default_timer()

	array=quicksort_median(arr, 0, len(arr),mediancomparison)
	end_time = timeit.default_timer() - start_time

	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		array) + " and The time taken to excute the 3 median quick  alogirthm is " + str(end_time))
	print(str(time))

	label.place(x=500,y=650)
def quicksort_medcompare(arr):
	mediancomparison = 0
	start_time = timeit.default_timer()

	array = quicksort_median(arr, 0, len(arr), mediancomparison)
	end_time = timeit.default_timer() - start_time
	label = tk.Label(root, text="Array is sorted and the final out put is " + str(
		arr) + " and The time taken to excute the 3 median quick  alogirthm is " + str(end_time))
	print("3quick"+str(end_time))

	label.place(x=500, y=650)


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Enter the list to be sorted', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))


Mergesort = tk.Button(root, text='Mergesort', command=mergesort)
Heapsort = tk.Button(root, text='Heapsort', command=heapsort)
Quicksort = tk.Button(root, text='Quicksort ', command=quicksort_main)

Insertionsort = tk.Button(root, text='Insertion sort ', command=insertionsort)

Selectionsort = tk.Button(root, text='Selection sort ', command=selectionsort)
Bubblesort = tk.Button(root, text='Bubble sort ', command=Bubblesort)
compareall = tk.Button(root, text='Compare All', command=compare)

threequicksort = tk.Button(root, text='Quicksort with 3 medians', command=quicksort_med)




name_label.place(x=100, y=10)
compareall.place(x=300, y=300)
name_entry.place(x=400, y=10)
threequicksort.place(x=550, y=100)

Mergesort.place(x=220, y=100)

Bubblesort.place(x=400, y=100)
Heapsort.place(x=20, y=100)
Quicksort.place(x=800, y=100)
Insertionsort.place(x=300, y=100)

Selectionsort.place(x=100, y=100)
# performing an infinite loop
# for the window to display
root.mainloop()
