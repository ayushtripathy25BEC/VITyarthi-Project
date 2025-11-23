import tkinter as tk
import math

# Function to evaluate expressions
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sin_func():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cos_func():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tan_func():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log_func():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry display
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=10, ipady=10, padx=10, pady=10)

# Buttons layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda x=button: button_click(x)

    tk.Button(button_frame, text=button, width=6, height=2, font=("Arial", 14),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Scientific buttons
sci_frame = tk.Frame(root)
sci_frame.pack(pady=10)

tk.Button(sci_frame, text="√", width=6, height=2, command=square_root).grid(row=0, column=0)
tk.Button(sci_frame, text="sin", width=6, height=2, command=sin_func).grid(row=0, column=1)
tk.Button(sci_frame, text="cos", width=6, height=2, command=cos_func).grid(row=0, column=2)
tk.Button(sci_frame, text="tan", width=6, height=2, command=tan_func).grid(row=1, column=0)
tk.Button(sci_frame, text="log", width=6, height=2, command=log_func).grid(row=1, column=1)
tk.Button(sci_frame, text="C", width=6, height=2, command=clear_entry).grid(row=1, column=2)

# Start the GUI
root.mainloop()