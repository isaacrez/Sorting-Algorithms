import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sortingAnimation as sA

class Window(tk.Frame):
    def __init__(self, master=None):
        self.sorting_method = "Heap"
        self.sorting_details = {
            'array_size': 32,
            'interval': 5,
            'step_size': 5
        }

        super().__init__(master)
        self.master = master
        self.create_window()
        self.create_animation()

    def create_window(self):
        self.master.title("Number Sorting Visualization")
        self.pack()
        self.create_side_bar()

    def client_exit(self):
        exit()

    def create_side_bar(self):
        frame = tk.Frame(self.master)
        frame['relief'] = 'sunken'
        frame.pack(side='left', anchor='n', expand=False, padx=5, pady=5)

        text = tk.Label(frame, text="Sorting Method")
        text.pack(fill='x')

        self.sorting_selector = ttk.Combobox(frame)
        self.sorting_selector['values'] = ["Bubble", "Insertion", "Heap", "Merge"]
        current_index = self.sorting_selector['values'].index(self.sorting_method)
        self.sorting_selector.current(current_index)
        self.sorting_selector['state'] = 'readonly'
        self.sorting_selector.insert(tk.END, self.sorting_method)

        self.sorting_selector.bind("<<ComboboxSelected>>", self.update_sorting_method)
        self.sorting_selector.pack(fill='x')

        vcmd = (frame.register(self.validate), '%P')
        input_label = ["Array size", "Interval time (ms)", "Step size"]
        input_id = ["array_size", "interval", "step_size"]

        for input_text, id in zip(input_label, input_id):
            current_entry = make_label_input_set(frame, input_text, self.sorting_details[id], validatecommand=vcmd)
            event_response = lambda event, id = id, current_entry = current_entry: \
                self.update_numeric_input(id, current_entry)
            current_entry.bind("<KeyRelease>", event_response)
            current_entry.bind("<FocusOut>", event_response)

        button = tk.Button(frame)
        button['text'] = 'Perform sort'
        button['cursor'] = 'hand2'
        button['command'] = self.run_animation
        button.pack(fill='x')

    def update_sorting_method(self, event):
        self.sorting_method = self.sorting_selector.get()

    def update_numeric_input(self, id: str, entry: tk.Entry):
        if entry.get():
            self.sorting_details[id] = int(entry.get())

    def validate(self, value_if_allowed):
        if value_if_allowed:
            try:
                value = int(value_if_allowed)
                if 0 < value <= 256:
                    return True
                return False
            except ValueError:
                return False
        return True

    def create_animation(self):
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.axis = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.master)
        self.canvas._tkcanvas.pack(fill='both', expand=True)
        self.animation = sA.Anim(self.figure,
                                 self.axis,
                                 sorting_name=self.sorting_method,
                                 array_size=self.sorting_details['array_size'],
                                 interval=self.sorting_details['interval'],
                                 steps_per=self.sorting_details['step_size'])

    def run_animation(self):
        self.animation.update_animation(sorting_name=self.sorting_method,
                                        array_size=self.sorting_details['array_size'],
                                        interval=self.sorting_details['interval'],
                                        steps_per=self.sorting_details['step_size'])
        self.animation.start_animation()
        self.canvas.draw()


def make_label_input_set(parent_frame: tk.Frame, label_text: str, initial_value: str = '8', validatecommand=None):
    frame = tk.Frame(parent_frame)
    frame.pack(anchor='w', fill='x')

    text = tk.Label(frame, text=label_text)
    text.pack(side='left')

    if validatecommand is None:
        entry = tk.Entry(frame)
    else:
        entry = tk.Entry(frame, validate='key', validatecommand=validatecommand)
    entry['justify'] = tk.RIGHT
    entry.insert(10, initial_value)
    entry.pack(anchor='e', expand=True)
    return entry

def create_UI():
    root = tk.Tk()
    app = Window(root)
    root.mainloop()