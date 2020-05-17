
import math
import numpy as np
import random


def merge_sort(num_array):
    # Breaks the array into size 1 or 2 sorted arrays, and then merges sorted arrays
    N = num_array.size
    if N == 1:
        return num_array
    elif N == 2:
        if num_array[1] < num_array[0]:
            num_array = _swap_indices(num_array, 0, 1)
        return num_array

    # Retrieve
    split = math.ceil(N/2)
    sorted1 = merge_sort(num_array[0:split])
    sorted2 = merge_sort(num_array[split:N])
    return _combine_sorted(sorted1, sorted2)


def _combine_sorted(sorted1, sorted2):
    # Linearly combines two sorted lists
    i = 0
    j = 0
    n1 = len(sorted1)
    n2 = len(sorted2)
    N = n1 + n2

    num_array = np.zeros(N)

    for pos in range(0, N):
        if i == n1:
            num_array[pos:N] = sorted2[j:n2]
            break
        if j == n2:
            num_array[pos:N] = sorted1[i:n1]
            break

        if sorted1[i] < sorted2[j]:
            num_array[pos] = sorted1[i]
            i += 1
        else:
            num_array[pos] = sorted2[j]
            j += 1

    return num_array


def quick_sort(num_array):
    #TODO: Develop iterative approach; recursion limit is hit very quickly
    n = num_array.size
    if n <= 1:
        return num_array
    if n == 2:
        if num_array[1] < num_array[0]:
            num_array = _swap_indices(num_array, 0, 1)
        return num_array

    pivot_index = random.randint(0, n-1)
    pivot = num_array[pivot_index]

    upper_partition = []
    lower_partition = []

    for i in range(n):
        if num_array[i] < pivot:
            lower_partition.append(num_array[i])
        else:
            upper_partition.append(num_array[i])

    upper_partition = quick_sort(np.array(upper_partition))
    lower_partition = quick_sort(np.array(lower_partition))
    num_array = np.hstack((lower_partition, upper_partition))
    return num_array



def insert_sort(num_array):
    n = num_array.size
    for i in range(1, n):
        j = i
        while j != 0 and num_array[j] < num_array[j-1]:
            _swap_indices(num_array, j-1, j)
            j -= 1
    return num_array


def bubble_sort(num_array):
    # Switches adjacent numbers until no additional swaps are necessary
    done = False
    n = num_array.size

    while not done:
        done = True
        for i in range(1, n):
            if num_array[i] < num_array[i-1]:
                num_array = _swap_indices(num_array, i - 1, i)
                done = False

        print(num_array)
    return num_array


def _swap_indices(num_array, index1, index2):
    # Switches the values at the given indexes for the array
    temp = num_array[index1]
    num_array[index1] = num_array[index2]
    num_array[index2] = temp
    return num_array


class HeapSort:
    def __init__(self, num_array):
        self.sort(num_array)

    def sort(self, num_array):
        # Allows user to easily sort a new set of values
        self.heap_size = num_array.size
        self.sorted_array = num_array
        self._heapify()
        self._sort()
        return self.sorted_array

    def get_sorted(self):
        # Allows user to request output after calculating it
        return self.sorted_array

    def _heapify(self):
        N = self.sorted_array.size
        for i in range(N):
            self._siftup(i)

    def _sort(self):
        # Handles sorting process; sorts in place
        while self.heap_size != 0:
            curr_val = self._pop()
            self.sorted_array[self.heap_size] = curr_val

    def _pop(self):
        head = self.sorted_array[0]
        self._siftdown()
        return head

    def _siftup(self, index):
        while index != 0:
            parent_index = math.floor((index - 1)/2)
            current_value = self.sorted_array[index]
            parent_value = self.sorted_array[parent_index]
            if current_value > parent_value:
                _swap_indices(self.sorted_array, index, parent_index)
            else:
                break
            index = parent_index

    def _siftdown(self):
        self.sorted_array[0] = self.sorted_array[self.heap_size-1]
        self.heap_size -= 1

        index = 0
        while index < self.heap_size/2 - 1:
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            parent_value = self.sorted_array[index]
            left_value = self.sorted_array[left_index]
            right_value = self.sorted_array[right_index]

            if parent_value < left_value or parent_value < right_value:
                if left_value < right_value:
                    _swap_indices(self.sorted_array, index, right_index)
                    index = right_index
                else:
                    _swap_indices(self.sorted_array, index, left_index)
                    index = left_index
            else:
                break
