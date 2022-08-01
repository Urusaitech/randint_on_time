from random import Random
from time import time
import tkinter as tk
from tkinter import ttk


def time_dependent_rng(start, end):
    # divide by 60 to bound generation to seconds
    timestamp = int(time()) // 60
    # generate seed
    random = Random(timestamp)
    # generate randint in between
    return random.randint(start, end)


def main():
    root = tk.Tk()
    main_frame = ttk.Frame(root, padding=10)
    main_frame.grid()

    app_name_label = ttk.Label(main_frame, text="Generate Rand Int")
    app_name_label.grid(column=0, row=0, columnspan=3)

    start_var = tk.StringVar(main_frame)
    ttk.Label(main_frame, text="Start").grid(column=0, row=1, columnspan=1)
    ttk.Entry(main_frame, width=20, textvariable=start_var).grid(column=1, row=1, columnspan=2)

    end_var = tk.StringVar(main_frame)
    ttk.Label(main_frame, text="End").grid(column=0, row=2, columnspan=1)
    ttk.Entry(main_frame, width=20, textvariable=end_var).grid(column=1, row=2, columnspan=2)

    result_var = tk.StringVar(main_frame)
    result_label = ttk.Label(main_frame, textvariable=result_var)
    result_label.grid(column=0, row=4, columnspan=3)

    def callback():
        start = start_var.get()
        end = end_var.get()
        try:
            end = int(end)
        except ValueError:
            result_var.set(f"Incorrect input:\nIn the 'start' impossible to convert '{end}' into int.")
            return
        if not start:
            start = 0
        else:
            try:
                start = int(start)
            except ValueError:
                result_var.set(f"Incorrect input:\nIn the 'end' impossible to convert '{start}' into int.")
                return
        if start >= end:
            result_var.set(f"Incorrect input:\nEnd should be lower than Start.")
            return
        res = time_dependent_rng(start, end)
        result_var.set(f"Rand int: {res}")
        return

    ttk.Button(main_frame, text="Generate!", command=callback).grid(column=0, row=3, columnspan=3)

    root.mainloop()


if __name__ == "__main__":
    main()
