import math
import numpy as np
import random


class Sorter():
    def __init__(self, num_array=[]):
        self.num_array = num_array
        self.comparisons = 0
        self.accesses = 0
        self.current_index = 0
        self.compare_index = -1
        self.done = False

    def set_array(self, num_array):
        self.num_array = num_array

    def get_array(self):
        return self.num_array

    @staticmethod
    def _combine_sorted(sorted1, sorted2):
        # Linearly combines two sorted lists
        i = 0
        j = 0
        n1 = len(sorted1)
        n2 = len(sorted2)
        N = n1 + n2

        combined = np.zeros(N)

        for pos in range(0, N):
            if i == n1:
                combined[pos:N] = sorted2[j:n2]
                break
            if j == n2:
                combined[pos:N] = sorted1[i:n1]
                break

            if sorted1[i] < sorted2[j]:
                combined[pos] = sorted1[i]
                i += 1
            else:
                combined[pos] = sorted2[j]
                j += 1

        return combined

    def _swap_indices(self, index1, index2):
        # Switches the values at the given indexes for the array
        temp = self.num_array[index1]
        self.num_array[index1] = self.num_array[index2]
        self.num_array[index2] = temp


class MergeSort(Sorter):
    def __init__(self, num_array=[]):
        super().__init__(num_array)
        self.partition_size = 2
        self.partition_index = 0
        self.current_index = 1
        self.compare_index = 0

    def sort_step(self, steps_taken):
        for i in range(steps_taken):
            if self.partition_size == 2:
                self._base_sort()
            elif self.partition_size/2 < self.num_array.size:
                self._standard_sort()
            else:
                self.done = True
                break

    # TODO: Allow sorting of combined values to be displayed
    def _standard_sort(self):
        i = self.partition_index
        sorted_size = int(self.partition_size/2)
        split = i + sorted_size
        sorted_sub_1 = self.num_array[i:split]
        sorted_sub_2 = self.num_array[split:i + self.partition_size]

        self.num_array[i:i+self.partition_size] = self._combine_sorted(sorted_sub_1, sorted_sub_2)
        self.partition_index += self.partition_size

        if self.num_array.size <= self.partition_index:
            self._next_partition()

    def _base_sort(self):
        i = self.current_index
        j = self.compare_index
        if self.num_array.size-1 < i:
            self._next_partition()
            return
        elif self.num_array[i] < self.num_array[j]:
            self._swap_indices(i, j)
        self._update_indices()

    def _update_indices(self):
        self.compare_index += self.partition_size
        self.current_index += self.partition_size

    def _next_partition(self):
        self.current_index = 0
        self.compare_index = -1
        self.partition_index = 0
        self.partition_size *= 2

    def merge_sort(self, num_array):
        # Breaks the array into size 1 or 2 sorted arrays, and then merges sorted arrays
        N = num_array.size
        if N == 1:
            return num_array
        elif N == 2:
            if num_array[1] < num_array[0]:
                num_array = self._swap_indices(0, 1)
            return num_array

        # Retrieve
        split = math.ceil(N / 2)
        sorted1 = self.merge_sort(num_array[0:split])
        sorted2 = self.merge_sort(num_array[split:N])
        return self._combine_sorted(sorted1, sorted2)


# TODO: Update to properly fit "Sorter" format
class QuickSort(Sorter):
    def __init__(self, num_array=[]):
        super().__init__(num_array)

    def quick_sort(self, num_array):
        # TODO: Develop iterative approach; recursion limit is hit very quickly
        n = num_array.size
        if n <= 1:
            return num_array
        if n == 2:
            if num_array[1] < num_array[0]:
                num_array = self._swap_indices(num_array, 0, 1)
            return num_array

        pivot_index = random.randint(0, n - 1)
        pivot = num_array[pivot_index]

        upper_partition = []
        lower_partition = []

        for i in range(n):
            if num_array[i] < pivot:
                lower_partition.append(num_array[i])
            else:
                upper_partition.append(num_array[i])

        upper_partition = self.quick_sort(np.array(upper_partition))
        lower_partition = self.quick_sort(np.array(lower_partition))
        num_array = np.hstack((lower_partition, upper_partition))
        return num_array


class InsertionSort(Sorter):
    def __init__(self, num_array=[]):
        super().__init__(num_array)
        # This holds the current position that's been last sorted
        self.position_index = 0

    def sort_step(self, steps_taken):
        for i in range(steps_taken):
            i = self.current_index
            j = self.compare_index

            # Identified a switch
            if self.num_array[i] < self.num_array[j]:
                self._swap_indices(i, j)
                self.current_index -= 1
                self.compare_index -= 1

                if self.compare_index < 0:
                    self._iterate_array()

            # Number is positioned appropriately
            else:
                self._iterate_array()

            # Finished sorting the num_array
            if self.position_index == self.num_array.size:
                self.done = True
                break

    def _iterate_array(self):
        self.position_index += 1
        self.current_index = self.position_index
        self.compare_index = self.position_index - 1


class BubbleSort(Sorter):
    def __init__(self, num_array=[]):
        super().__init__(num_array)
        self._changed = False

    def sort_step(self, steps_taken):
        for i in range(steps_taken):
            self._update_index()
            if not self.done:
                i = self.current_index
                j = self.compare_index
                if self.num_array[i] < self.num_array[j]:
                    self._changed = True
                    self._swap_indices(i, i - 1)

    def _update_index(self):
        self.current_index += 1
        n = self.num_array.size
        if self.current_index == n:
            if not self._changed:
                self.done = True
            else:
                self._changed = False
                self.current_index = 1
        self.compare_index = self.current_index - 1


class HeapSort(Sorter):
    def __init__(self, num_array=[]):
        super().__init__(num_array)
        self.heap_size = 0
        self.is_heap = False

    def sort_step(self, steps_taken):
        for i in range(steps_taken):
            if not self.is_heap:
                self._heapify()
            if self.is_heap:
                self._sort()

    def _sort(self):
        if 0 < self.heap_size:
            self._pop()
            self.current_index = self.heap_size
        else:
            self.done = True

    def _pop(self):
        self.heap_size -= 1
        head = self.num_array[0]
        self._siftdown()
        self.num_array[self.heap_size] = head

    def _siftdown(self):
        self.num_array[0] = self.num_array[self.heap_size]
        index = 0

        while index <= self.heap_size / 2 - 1:
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            parent_value = self.num_array[index]
            left_value = self.num_array[left_index]
            right_value = self.num_array[right_index]

            if parent_value < left_value or parent_value < right_value:
                if left_value < right_value:
                    self._swap_indices(index, right_index)
                    index = right_index
                else:
                    self._swap_indices(index, left_index)
                    index = left_index
            else:
                break

    def _heapify(self):
        if self.num_array.size == self.current_index:
            self.heap_size = self.num_array.size
            self.is_heap = True
        else:
            self._siftup(self.current_index)
            self.current_index += 1

    def _siftup(self, index):
        while index != 0:
            parent_index = math.floor((index - 1) / 2)
            current_value = self.num_array[index]
            parent_value = self.num_array[parent_index]
            if current_value > parent_value:
                self._swap_indices(index, parent_index)
            else:
                break
            index = parent_index
