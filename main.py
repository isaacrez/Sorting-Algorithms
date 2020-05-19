
import matplotlib.pyplot as plt

import numberSorting as nS
import sortingAnimation as sA

# PARAMETERS
array_size = 10
interval = 1

# All completely implemented methods are below
# sorting_object = nS.InsertionSort()
# sorting_object = nS.BubbleSort()
sorting_object = nS.HeapSort()

animation_storage = sA.Anim(sorting_object, array_size, interval)
plt.show()
