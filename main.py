
import matplotlib.pyplot as plt

import numberSorting as nS
import sortingAnimation as sA

array_size = 8
bs = nS.BubbleSort()
x = sA.Anim(bs, array_size)
plt.show()
