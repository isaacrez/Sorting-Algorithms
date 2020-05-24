
import numpy as np
import matplotlib
import matplotlib.animation as animation
matplotlib.use("Agg")

import randomArrays as ra
import numberSorting as ns

class Anim:
    def __init__(self, figure, subplot, sorting_name: str, array_size=10, interval=200, steps_per=1):
        self.fig = figure
        self.ax = subplot
        self.set_sorting_obj(sorting_name)
        self.array_size = array_size
        self.interval = interval
        self.steps_per = steps_per
        self.animator = None

    def update_animation(self, sorting_name: str = None, array_size: int = None, interval: int = None, steps_per: int = None):
        if not (sorting_name is None):
            self.set_sorting_obj(sorting_name)
        if not (array_size is None):
            self.array_size = array_size
        if not (interval is None):
            self.interval = interval
        if not (steps_per is None):
            self.steps_per = steps_per

    def set_sorting_obj(self, sorting_name: str):
        switch = {
            "Heap": ns.HeapSort,
            "Merge": ns.MergeSort,
            "Bubble": ns.BubbleSort,
            "Insertion": ns.InsertionSort
        }
        generator = switch.get(sorting_name, "Invalid name")
        if generator is str:
            print(sorting_name, "is not a valid sorting option")
        else:
            self.sorting_obj = switch[sorting_name]()

    def start_animation(self):
        self.initial_array(self.array_size)

        if not (self.animator is None):
            self.animator.event_source.stop()

        self.animator = animation.FuncAnimation(self.fig,
                                      self.animate,
                                      repeat=False,
                                      interval=self.interval)

        # TODO: Add ability to save animations
        # Writer = animation.writers['ffmpeg']
        # writer = Writer(fps=15, meta=dict(artist='Isaac Rezey'), bitrate=1800)
        # self.animator.save('sample.mp4', writer=writer)

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
        self.ax.set_xlim(0, element_count)
        self.ax.set_ylim(0, 100)

        curr_index = self.sorting_obj.current_index
        self.ax.get_children()[curr_index].set_color('c')

        comp_index = self.sorting_obj.compare_index
        if 0 <= comp_index:
            self.ax.get_children()[comp_index].set_color('g')