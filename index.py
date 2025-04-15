import tkinter as tk
from tkinter import font

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def button_click(number):
    current = entry.get()
    if current == "0" or current == "Cannot divide by zero!": # LOL look at wikipedia page Division By Zero.
        entry.delete(0, tk.END)
        entry.insert(0, number)
    else:
        entry.insert(tk.END, number)

def clear_button():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

def backspace_button():
    current = entry.get()
    if len(current) > 1:
        entry.delete(len(current) - 1)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "0")

def calculate():
    try:
        expression = entry.get()
        def solve(expression):
            parts = []
            num = ""
            for char in expression:
                if char.isdigit() or char == '.':
                    num += char
                else:
                    if num:
                        parts.append(float(num))
                        num = ""
                    parts.append(char)
            if num:
                parts.append(float(num))

            def calculate_mult_div(sub_expression):
                new_sub_expression = []
                i = 0
                while i < len(sub_expression):
                    if sub_expression[i] == '*':
                        new_sub_expression[-1] = new_sub_expression[-1] * sub_expression[i+1]
                        i += 2
                    elif sub_expression[i] == '/':
                        if sub_expression[i+1] == 0:
                           return "Cannot divide by zero!"
                        new_sub_expression[-1] = new_sub_expression[-1] / sub_expression[i+1]
                        i += 2
                    else:
                        new_sub_expression.append(sub_expression[i])
                        i += 1
                return new_sub_expression

            md_solved = calculate_mult_div(parts)
            if type(md_solved) == str:
                return md_solved
            result = md_solved[0]
            for i in range(1, len(md_solved), 2):
                if md_solved[i] == '+':
                    result += md_solved[i+1]
                elif md_solved[i] == '-':
                    result -= md_solved[i+1]
            return result

        result = solve(expression)
        entry.delete(0, tk.END)
        if isinstance(result, str):
            entry.insert(0, result)
        else:
            entry.insert(0, str(result))

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Syntax Error")

window = tk.Tk()
window.title("Calculator")



window.geometry("300x400")
window.resizable(False, False)

my_font = font.Font(size=16)

entry = tk.Entry(window, width=15, font=my_font, borderwidth=5, justify=tk.RIGHT)
entry.insert(0, "0")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_params = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("/", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("del", 5, 1), (" ", 5, 2), (" ", 5, 3)
]

buttons = {}
for (text, row, col) in button_params:
    if text == "C":
        button = tk.Button(window, text=text, command=clear_button, font=my_font, bg="#FF6B6B", fg="white")
    elif text == "del":
        button = tk.Button(window, text=text, command=backspace_button, font=my_font, bg="#FF6B6B", fg="white")
    elif text == "=":
        button = tk.Button(window, text=text, command=calculate, font=my_font, bg="#4CAF50", fg="white")
    elif text == " ":
        button = tk.Button(window, text=text, font=my_font, state=tk.DISABLED)
    else:
        button = tk.Button(window, text=text, command=lambda t=text: button_click(t), font=my_font)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons[text] = button

for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()
