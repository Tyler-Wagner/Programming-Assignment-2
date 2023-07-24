"""
Author: Tyler Wagner
Date Created: 7-21-23
Edited By: Tyler Wagner
Edited On: 7-21-23
"""

import tkinter as tk

def window():

    window = tk.Tk()
    window.title("Test Window")

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    x_offset, y_offset = 200, 80
        

    window.mainloop()

