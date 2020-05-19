
import matplotlib.pyplot as plt

import numberSorting as nS
import sortingAnimation as sA

# PARAMETERS
array_size = 32
interval = 5
steps_per = 5

# All completely implemented methods are below
sorting_object = nS.InsertionSort()
# sorting_object = nS.BubbleSort()
# sorting_object = nS.HeapSort()
# sorting_object = nS.MergeSort()

animation_storage = sA.Anim(sorting_object, array_size, interval, steps_per)
plt.show()
