"""
Author: Tyler Wagner
Date Created: 7-21-23
Edited By: Tyler Wagner
Edited On: 7-21-23
"""

import tkinter as tk

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def draw_tree(node, canvas, x, y, x_offset, y_offset):
    if node is not None:
        canvas.create_oval(x-15, y-15, x+15, y+15, fill="white", outline="black")
        canvas.create_text(x, y, text=str(node.value), fill="black")

        if node.left is not None:
            canvas.create_line(x, y, x - x_offset, y + y_offset, fill="black")
            draw_tree(node.left, canvas, x - x_offset, y + y_offset, x_offset/2, y_offset)

        if node.right is not None:
            canvas.create_line(x, y, x + x_offset, y + y_offset, fill="black")
            draw_tree(node.right, canvas, x + x_offset, y + y_offset, x_offset/2, y_offset)

def main():
    root = create_tree()

    window = tk.Tk()
    window.title("Tree Visualization")

    canvas = tk.Canvas(window, width=600, height=400, bg="white")
    canvas.pack()

    x_offset, y_offset = 200, 80
    draw_tree(root, canvas, 300, 40, x_offset, y_offset)

    window.mainloop()

if __name__ == "__main__":
    main()