
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import randomArrays as ra
import numberSorting as ns

class Anim:
    def __init__(self, sorting_obj: ns.Sorter, array_size=10, interval=200, steps_per=1):
        fig, self.ax = plt.subplots()
        self.sorting_obj = sorting_obj
        self.initial_array(array_size)
        self.steps_per = steps_per
        self.animator = FuncAnimation(fig, self.animate, repeat=False, interval=interval)

    def initial_array(self, array_size):
        self.ax.set_xlim((0, array_size))
        self.ax.set_ylim((0, 100))
        random_data = ra.generate_random_number_array(array_size)
        self.sorting_obj.set_array(random_data)

    def animate(self, i):
        # Determine if stopping
        self.sorting_obj.sort_step(self.steps_per)
        if self.sorting_obj.done:
            self.animator.event_source.stop()
        self.ax.clear()

        # Update plot
        element_count = self.sorting_obj.get_array().size
        x_data = np.arange(0, element_count)
        y_data = self.sorting_obj.get_array()
        self.ax.bar(x_data, y_data, align="edge", width=1)

        curr_index = self.sorting_obj.current_index
        self.ax.get_children()[curr_index].set_color('c')

        comp_index = self.sorting_obj.compare_index
        if 0 <= comp_index:
            self.ax.get_children()[comp_index].set_color('g')