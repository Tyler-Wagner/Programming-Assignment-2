"""
Author: Tyler Wagner
Date Created: 7-21-23
Edited By: Tyler Van Pelt
Edited On: 7-28-23
"""


import tkinter as tk

def draw_decision_tree(canvas, node, x, y, depth=0):
    if node is None:
        return

    # Draw the current node
    if node.attribute is not None and node.threshold is not None:
        node_size = 30
        canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, fill="blue")
        text_x = x - 30
        text_y = y - 10

        # Convert node.threshold to float if it is numeric
        if node.threshold.replace('.', '', 1).isdigit():
            node.threshold = float(node.threshold)
            canvas.create_text(text_x, text_y, text=f'Attr: {node.attribute}\nThresh: {node.threshold:.2f}', fill="black")
        else:
            canvas.create_text(text_x, text_y, text=f'Attr: {node.attribute}\nThresh: {node.threshold}', fill="black")

    if node.left is not None:
        x_left = x - 100 / (2 ** depth)
        y_left = y + 60
        canvas.create_line(x, y, x_left, y_left, fill="red")
        draw_decision_tree(canvas, node.left, x_left, y_left, depth + 1)

    if node.right is not None:
        x_right = x + 100 / (2 ** depth)
        y_right = y + 60
        canvas.create_line(x, y, x_right, y_right, fill="blue")
        draw_decision_tree(canvas, node.right, x_right, y_right, depth + 1)

def display_results_window(predictions_test, predictions_new_data, root_node):
    window = tk.Tk()
    window.title("Decision Tree Results")

    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()

    # Test data predictions
    test_result_label = tk.Label(window, text="Predicted class labels for test data:")
    test_result_label.pack()

    test_results_var = tk.StringVar()
    test_results_var.set(predictions_test)
    test_results_label = tk.Label(window, textvariable=test_results_var)
    test_results_label.pack()

    # New data predictions
    new_data_result_label = tk.Label(window, text="Predicted class labels for new data:")
    new_data_result_label.pack()

    new_data_results_var = tk.StringVar()
    new_data_results_var.set(predictions_new_data)
    new_data_results_label = tk.Label(window, textvariable=new_data_results_var)
    new_data_results_label.pack()

    # Draw the decision tree
    draw_decision_tree(canvas, root_node, 400, 40)

    window.mainloop()

