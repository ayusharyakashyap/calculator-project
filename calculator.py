from tkinter import *
from math import factorial, pi, sqrt, log, sin, cos, tan

root = Tk()
root.title('Calculator')

# It keeps the track of the current position on the input text field
i = 0

# Receives the digit as parameter and displays it on the input field
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

# Calculate function scans the string to evaluates and display it
def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# Function to clear the input field 
def clear_all():
    display.delete(0, END)

# Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the factorial and display it
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the square root and display it
def sqrt_operation():
    entire_string = display.get()
    try:
        result = sqrt(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the logarithm and display it
def log_operation():
    entire_string = display.get()
    try:
        result = log(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the sine and display it
def sin_operation():
    entire_string = display.get()
    try:
        result = sin(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the cosine and display it
def cos_operation():
    entire_string = display.get()
    try:
        result = cos(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the tangent and display it
def tan_operation():
    entire_string = display.get()
    try:
        result = tan(float(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function to calculate the power of 10 and display it
def power_of_ten():
    entire_string = display.get()
    try:
        result = 10**float(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# --------------------------------------UI Design ---------------------------------------------

# Adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

# Code to add buttons to the Calculator

Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2, sticky=N+S+E+W)

# Adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text=".", command=lambda: get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N+S+E+W)

# Adding new operations
Button(root, text="pi", command=lambda: get_variables(pi)).grid(row=2, column=4, sticky=N+S+E+W)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N+S+E+W)

Button(root, text="undo", command=lambda: undo()).grid(row=2, column=5, sticky=N+S+E+W)
Button(root, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky=N+S+E+W)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N+S+E+W)

Button(root, text="sqrt", command=lambda: sqrt_operation()).grid(row=6, column=0, sticky=N+S+E+W)
Button(root, text="log", command=lambda: log_operation()).grid(row=6, column=1, sticky=N+S+E+W)
Button(root, text="sin", command=lambda: sin_operation()).grid(row=6, column=2, sticky=N+S+E+W)
Button(root, text="cos", command=lambda: cos_operation()).grid(row=6, column=3, sticky=N+S+E+W)
Button(root, text="tan", command=lambda: tan_operation()).grid(row=6, column=4, sticky=N+S+E+W)
Button(root, text="10^x", command=lambda: power_of_ten()).grid(row=6, column=5, sticky=N+S+E+W)

Button(root, text="=", command=lambda: calculate()).grid(row=7, columnspan=6, sticky=N+S+E+W)

root.mainloop()
