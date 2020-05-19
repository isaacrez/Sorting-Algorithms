
import matplotlib.pyplot as plt

import numberSorting as nS
import sortingAnimation as sA

array_size = 25
interval = 1

bs = nS.InsertionSort()
x = sA.Anim(bs, array_size, interval)
plt.show()
