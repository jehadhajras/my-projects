import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Variable to store the input expression
expression = ""

# Function to update the input field
def press(key):
    global expression
    expression += str(key)
    entry_var.set(expression)

# Function to calculate the result
def calculate():
    try:
        global expression
        result = eval(expression)  # Evaluate the expression
        expression = str(result)
        entry_var.set(expression)
    except:
        entry_var.set("Error")
        expression = ""

# Function to clear the input
def clear():
    global expression
    expression = ""
    entry_var.set(expression)

# Function to calculate the square root
def sqrt():
    global expression
    try:
        result = math.sqrt(float(expression))  # Calculate square root
        expression = str(result)
        entry_var.set(expression)
    except:
        entry_var.set("Error")
        expression = ""

# Define the user interface
entry_var = tk.StringVar()

# Input display (Entry widget)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sqrt', 5, 0), ('C', 5, 1)
]

# Add the buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=clear)
    elif text == "sqrt":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=sqrt)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=lambda key=text: press(key))

    button.grid(row=row, column=col)

# Run the application
root.mainloop()
